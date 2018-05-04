from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.decorators import permission_classes
from rest_framework import permissions
import pandas
import pymongo
import json

@permission_classes((permissions.AllowAny,))
class FileUploadView(APIView):
	parser_classes = (FileUploadParser,)

	# authentication_classes = (JSONWebTokenAuthentication, )
	
	def post(self, request, format=None):
		file_obj = request.data['file']

		dataframe = pandas.read_csv(file_obj.file, error_bad_lines=False)
		json_data = json.loads(dataframe.to_json(orient="records"))

		
		mongo_client = pymongo.MongoClient('mongo', 27017)
		mongo_db = mongo_client['database_teste']
		collection = mongo_db['collection_teste']

		# 	# Inserindo no banco 
		collection.insert(json_data)
		return Response(status=201)