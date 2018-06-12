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
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

DB_NAME = 'mongo'


def get_session_id():
    return login_metabase()


def get_dashboard(pk):
    dashboard = Dashboard.objects.get(pk=pk)
    return dashboard


@permission_classes((permissions.AllowAny,))
class DashboardIframes(APIView):
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

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

    def post(self, request, pk, format=None):
        session_id = get_session_id()
        database_id = get_database_id(DB_NAME)
        dashboard = get_dashboard(pk)
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
            "visualization_settings": {}

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
            iframe = serializer.save()
            iframe.uuid = public_card.json()['uuid']
            iframe.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)

    def get(self, request, pk, format=None):
        iframes = Iframe.objects.filter(dashboard_id=pk)
        serializer = IframeSerializerList(iframes, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)


@permission_classes((permissions.AllowAny,))
class DashboardFields(APIView):
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    def get(self, request, pk, format=None):
        session_id = get_session_id()
        database_id = get_database_id(DB_NAME)
        dashboard = get_dashboard(pk)
        table_name = "collection_{}".format(dashboard.project.id)
        table_id = get_table_id(database_id, table_name)

        header = {'Cookie': 'metabase.SESSION_ID=' + session_id}

        url_get_fields = MB_URL + '/table/{}/query_metadata'.format(table_id)

        data = requests.get(url_get_fields, headers=header)
        ndata = data.json()

        return Response(status=status.HTTP_200_OK, data=ndata)
