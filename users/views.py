from __future__ import unicode_literals
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from users.serializers import UserCreateSerializer, UserUpdateSerializer
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from django.http import Http404
from django.contrib.auth.models import User
# Create your views here.


@permission_classes((permissions.AllowAny,))
class UserList(APIView):

    def get(self, request, format=None):

        users = User.objects.all()
        serializer = UserCreateSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = UserCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserCreateSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk=pk)
        serializer = UserUpdateSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
