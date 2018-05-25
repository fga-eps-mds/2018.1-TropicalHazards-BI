from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import status
    


@permission_classes((permissions.AllowAny,))
class DashboardIframes(APIView):


    def post(self, request, format=None):
        # name = request.data['name']
        # display_type = request.data['display_type']
        # fields = request.data['fields']
        data_base_id = 2 #usando o mongo como database do metabase
        table_id = 12 #usando a collection_Exemplo.csv

        # r = requests.post("http://metabase:3000/api/session",
        #                   headers={"Content-Type": "application/json"},
        #                   json={"username": "joaok8@gmail.com",
        #                         "password": "jpgomes250595"})

        # print(r.json())
        header = {'Cookie': 'metabase.SESSION_ID=6f199c99-88a8-49bf-b7c8-baaae72ac652'}
        # .format(r.json()['id']) 
        print (header)



        data = {
            "name": "card1",
            "display": "table",
            "dataset_query": {
                "database": data_base_id,
                "type": "query",
                "query": {
                    "source_table": table_id,                                                    
                }
            },
            "visualization_settings": {}                 

        }
        card = requests.post("http://metabase:3000/api/card",
                            json=data,
                            headers=header
                            )
        print(card.json())

        public_card = requests.post("http://metabase:3000/api/card/{}/public_link".format(card.json()['id']),
                                    headers=header)
        print(public_card.json())
        # .format(card.json()['id']), json={})        
        # public_card = requests.post("http://metabase:3000/api/card/{}/public_link".format(card.json()['id']), json={})        

        # print(public_card.json())

        return Response(status=status.HTTP_200_OK)