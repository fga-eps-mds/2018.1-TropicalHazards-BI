import pandas
import pymongo
import json
import os
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from import_data.serializers import ImportDataSerializer
from rest_framework import status


@permission_classes((permissions.AllowAny,))
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    # authentication_classes = (JSONWebTokenAuthentication, )

    def post(self, request, format=None):
        file_obj = request.data['file']
        project_id = request.data['project']
        # Fix temporária por probelmas com forma aappend
        to_remove_list_fields = json.loads(request.data['headers'])
        to_define_list_fields = json.loads(request.data['define'])
        # Problemas na passagem de tipo de dado como string
        # type_list_fields = json.loads(request.data['types'])
        type_list_fields = []

        serializer = ImportDataSerializer(data=request.data)
        if serializer.is_valid():
            file_path = '/code/tmp/' + file_obj.name
            if not file_obj.name.endswith('.csv'):
                return Response(status=status.HTTP_400_BAD_REQUEST)

            else:
                with default_storage.open(file_path, 'wb+') as dest:
                    for chunk in file_obj.chunks():
                        dest.write(chunk)

                dataframe = pandas.read_csv(file_path, header=0)

                dataframe = dataframe.drop(to_remove_list_fields, axis=1)

                for dfield, type in zip(to_define_list_fields,
                                        type_list_fields):
                    try:
                        dataframe[dfield] = dataframe[dfield].astype(type)
                        break
                    except ValueError:
                        return Response(serializer.errors,
                                        status=status.
                                        HTTP_400_BAD_REQUEST)
                print(dataframe.dtypes)
                json_data = json.loads(dataframe.to_json(orient="records"))

                mongo_client = pymongo.MongoClient('mongo', 27017)
                mongo_db = mongo_client['main_db']
                collection = mongo_db['collection_' + project_id]
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
                print(type(doc))
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
