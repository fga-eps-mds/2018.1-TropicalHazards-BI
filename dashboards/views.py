from .models import Dashboard
from .serializers import DashboardSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.authentication import BasicAuthentication
# from django.contrib.auth.models import Project
# from django.core import serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@permission_classes((IsAuthenticatedOrReadOnly, ))
class DashboardList(APIView):
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    def get(self, request, format=None):
        dashboards = Dashboard.objects.all()
        serializer = DashboardSerializer(dashboards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DashboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticatedOrReadOnly, ))
class DashboardDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    def get_object(self, pk):
        try:
            return Dashboard.objects.get(pk=pk)
        except Dashboard.DoesNotExist:
            raise Http404

    def get(self, request, pk, fomrat=None):
        dashboard = self.get_object(pk)
        serializer = DashboardSerializer(dashboard)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dashboard = self.get_object(pk)
        serializer = DashboardSerializer(dashboard, data=request.data)
        if serializer.is_valid() and (request.user == dashboard.user or
           request.user == dashboard.project.user):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dashboard = self.get_object(pk)
        if (request.user ==
           dashboard.user or request.user == dashboard.project.user):
            dashboard.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
