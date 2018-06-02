import pandas
import pymongo
import json
from metabase import utils
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.exceptions import ValidationError

from import_data.serializers import ImportDataSerializer


def connect_mongo(engine=pymongo, host='mongo', port=27017):
    mongo_client = engine.MongoClient(host, port)
    mongo_db = mongo_client['main_db']

    return mongo_db


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    mongo_db = connect_mongo()

    authentication_classes = (JSONWebTokenAuthentication, )

    def save_file_tmp(self, file, file_path):
        with open(file_path, 'wb') as dest:
            for chunk in file.chunks():
                dest.write(chunk)
            dest.close()

    def save_on_mongo(self, data, project_id):
        """
        Return True when saved False when not.
        Any error on data format will return False
        """
        try:
            collection = self.mongo_db['collection_' + str(project_id)]
            result = collection.insert_many(data)
            result = result.acknowledged
        except TypeError:
            result = False
        return result

    def check_file_type(self, file):
        if file.name.endswith('.csv'):
            return 'csv'
        else:
            raise ValidationError("Type of file not supported")

    def create_data_frame(self, file_path, file_type, **kwargs):
        if file_type is 'csv':
            sep = kwargs.get('sep', ',')
            return pandas.read_csv(file_path, header=0, sep=sep)

    def treat_bool_column(self, dataframe, header):
        dataframe[header['name']].replace(to_replace=header['true'],
                                          value=True, inplace=True)
        dataframe[header['name']].replace(to_replace=header['false'],
                                          value=False, inplace=True)

    def treat_upper_lower_case(self, dataframe, header):
        if header['transform'] == 'upper':
            dataframe[header['name']] =\
                dataframe[header['name']].str.upper()
        elif header['transform'] == 'lower':
            dataframe[header['name']] =\
                dataframe[header['name']].str.lower()
        return dataframe

    def type_conversion(self, dataframe, header):
        try:
            dataframe[header['name']] = dataframe[header['name']].\
                astype(header['type'])
        except ValueError:
            raise ValidationError("Type conversion failed")
        return dataframe

    def post(self, request, format=None):
        file_obj = request.data['file']
        project_id = int(request.data['project'])

        headersList = json.loads(request.data['headers'])

        serializer = ImportDataSerializer(data={'project': project_id})

        if serializer.is_valid():
            file_type = self.check_file_type(file_obj)

            file_path = '/code/tmp/' + file_obj.name
            self.save_file_tmp(file_obj, file_path)

            dataframe = self.create_data_frame(file_path, file_type)

            for header in headersList:
                if header['selected'] is False:
                    dataframe = dataframe.drop(header['name'], axis=1)
                else:
                    if header['type'] == 'bool':
                        self.treat_bool_column(dataframe, header)

                    dataframe = self.type_conversion(dataframe, header)
                    dataframe = self.treat_upper_lower_case(dataframe, header)

            json_data = json.loads(dataframe.to_json(orient="records"))

            if self.save_on_mongo(json_data, project_id):
                serializer.save()
                os.remove(file_path)

                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            else:
                return Response("Data format error",
                                status=status.HTTP_400_BAD_REQUEST)
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
