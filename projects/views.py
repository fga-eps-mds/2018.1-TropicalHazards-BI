from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from TropicalHazards_BI.utils import connect_mongo
from projects.models import Project
from projects.filters import ProjectFilter
from projects.serializers import ProjectSerializer
from metabase import utils


@permission_classes((IsAuthenticatedOrReadOnly,))
class ProjectList(generics.ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = ProjectFilter
    mongo_db = connect_mongo()

    def get(self, request, format=None):
        tag_name = self.request.query_params.get('tag_name', None)
        if tag_name is None:
            projects = Project.objects.all()
        else:
            projects = Project.objects.filter(tags__name=tag_name)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            self.mongo_db.create_collection('collection_' + str(project.id))
            db_id = utils.get_database_id('mongo')
            if(utils.sync_schema(db_id)):
                table_id = utils.get_table_id(db_id, 'collection_'
                                              + str(project.id))
                project.table_id = table_id
                project.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_503_SERVICE_UNAVAILABLE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((IsAuthenticated,))
class ProjectDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

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
        if serializer.is_valid() and request.user == project.user:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        if request.user == project.user:
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
