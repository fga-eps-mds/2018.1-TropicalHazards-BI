
from .models import Project
from projects.serializers import ProjectSerializer
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
from rest_framework.permissions import IsAuthenticated


@permission_classes((IsAuthenticated, ))
class ProjectList(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = ProjectSerializer(data=request.data)
        request.data['user'] = request.user.id

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated, ))
class ProjectDetail(APIView):
    def get_object(self, pk):

        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk=pk)
        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
