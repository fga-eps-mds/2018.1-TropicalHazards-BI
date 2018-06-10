import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import status

from metabase.utils import login_metabase
from metabase.utils import get_database_id
from metabase.utils import get_table_id
from metabase.utils import MB_URL
from metabase.serializers import IframeSerializerCreate
from metabase.serializers import IframeSerializerList
from metabase.models import Iframe
from dashboards.models import Dashboard

DB_NAME = 'mongo'


@permission_classes((permissions.AllowAny,))
class DashboardIframes(APIView):

    def get_session_id(self):
        return login_metabase()

    def get_dashboard(self, pk):
        dashboard = Dashboard.objects.get(pk=pk)

        return dashboard

    def create_card_metabase(self, data, header):
        url_card = MB_URL + '/card'
        card = requests.post(url_card, json=data,
                             headers=header)
        if card.status_code == 200:
            return card
        else:
            raise Exception("Could not create the card on metabase")

    def make_card_public(self, id, header):
        url_public_card = MB_URL + '/card/{}/public_link'.format(id)

        public_card = requests.post(url_public_card, headers=header)

        if public_card.status_code == 200:
            return public_card
        else:
            raise Exception("Could not make the card public on metabase")

    def make_visualization_settings(self, display, dimension, metric):
        if display == "pie":
            data = {
                "pie.metric": metric,
                "pie.dimension": dimension
            }
        else:
            data = {
                "graph.dimensions": dimension,
                "graph.metrics": metric
            }
        return data

    def post(self, request, pk, format=None):
        session_id = self.get_session_id()
        database_id = get_database_id(DB_NAME)
        dashboard = self.get_dashboard(pk)
        table_name = "collection_{}".format(dashboard.project.id)
        table_id = get_table_id(database_id, table_name)

        header = {'Cookie': 'metabase.SESSION_ID=' + session_id}
        data = {
            "name": request.data['name'],
            "display": request.data['display'],
            "dataset_query": {
                "database": database_id,
                "type": "query",
                "query": {
                    "source_table": table_id,
                }
            },
            "visualization_settings": self.make_visualization_settings(
                                      request.data['display'],
                                      request.data['dimension'],
                                      request.data['metric'])

        }

        iframe_data = {
                "name": request.data['name'],
                "user": request.user.id,
                "dashboard": dashboard.id,
        }

        serializer = IframeSerializerCreate(data=iframe_data)

        if serializer.is_valid():
            card = self.create_card_metabase(data, header)
            public_card = self.make_card_public(card.json()['id'], header)
            uuid = public_card.json()['uuid']
            iframe_data = {
                "name": request.data['name'],
                "user": request.user.id,
                "dashboard": dashboard.id,
                "uuid": uuid,
            }
            serializer = IframeSerializerCreate(data=iframe_data)            
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

    def get(self, request, pk, format=None):
        iframes = Iframe.objects.filter(dashboard_id=pk)
        serializer = IframeSerializerList(iframes, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
