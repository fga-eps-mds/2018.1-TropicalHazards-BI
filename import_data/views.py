import pandas
import pymongo
import json
import os
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from import_data.serializers import ImportDataSerializer
from rest_framework import status

from projects.models import Project


@permission_classes((permissions.AllowAny,))
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # authentication_classes = (JSONWebTokenAuthentication, )

    def post(self, request, format=None):
        file_obj = request.data['file']
        project_id = int(request.data['project'])

        headersList = json.loads(request.data['headers'])

        serializer = ImportDataSerializer(data={'project': project_id})
        if serializer.is_valid():
            file_path = '/code/tmp/' + file_obj.name
            if not file_obj.name.endswith('.csv'):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                with open(file_path, 'wb') as dest:
                    for chunk in file_obj.chunks():
                        dest.write(chunk)
                    dest.close()

                    dataframe = pandas.read_csv(file_path, header=0)
                    # true_values=headersList['true'],
                    # false_values=headersList['false'])

                    for header in headersList:
                        if header['selected'] is False:
                            dataframe = dataframe.drop(header['name'], axis=1)
                        else:
                            if header['type'] == 'bool':
                                dataframe[header['name']] =\
                                    dataframe[header['name']].\
                                    replace(to_replace=header['true'],
                                            value=True)
                                dataframe[header['name']] =\
                                    dataframe[header['name']].\
                                    replace(to_replace=header['false'],
                                            value=False)
                            try:
                                dataframe[header['name']] =\
                                    dataframe[header['name']].\
                                    astype(header['type'])
                            except ValueError:
                                return Response(serializer.errors,
                                                status=status.
                                                HTTP_400_BAD_REQUEST)
                            if header['transform'] == 'upper':
                                dataframe[header['name']] =\
                                    dataframe[header['name']].str.upper()
                            elif header['transform'] == 'lower':
                                dataframe[header['name']] =\
                                    dataframe[header['name']].str.lower()

                json_data = json.loads(dataframe.to_json(orient="records"))

                mongo_client = pymongo.MongoClient('mongo', 27017)
                mongo_db = mongo_client['main_db']
                collection = mongo_db['collection_' + str(project_id)]
                collection.insert(json_data)
                serializer.save()
                os.remove(file_path)

                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class FileUploadViewDetail(APIView):

    def get(self, request, pk, format=None):
        mongo_client = pymongo.MongoClient('mongo', 27017)
        mongo_db = mongo_client['main_db']
        collection = mongo_db['collection_' + str(pk)]
        if collection.count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            elements = collection.find({})
            json_docs = []
            for doc in elements:
                # Remove o campo _id do elemento, pois ele não é serializável
                del(doc['_id'])
                json_docs.append(doc)
            # O campo json_docs já está no formato JSON
            return Response(json_docs, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        remove_field = request.data['remove_field']
        mongo_client = pymongo.MongoClient('mongo', 27017)
        mongo_db = mongo_client['main_db']
        collection = mongo_db['collection_' + str(pk)]
        if collection.count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            collection.update({}, {'$unset': {remove_field: 1}}, multi=True)
