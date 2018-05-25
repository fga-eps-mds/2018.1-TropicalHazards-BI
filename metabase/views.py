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
        # data_base_id = 2

        r = requests.post("http://metabase:3000/api/session",
                          headers={"Content-Type": "application/json"},
                          json={"username": "andrebargas@gmail.com",
                                "password": "1234baba"})
        print(r.json())

        return Response(status=status.HTTP_200_OK)