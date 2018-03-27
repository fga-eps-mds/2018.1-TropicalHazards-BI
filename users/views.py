from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics
from users.serializers import UserSerializer
from django.contrib.auth.models import User


def create_user(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = UserSerializer(data=data)
        if serializers.is_valid():
            serializers.save
            return JsonResponse(serializers.data, status=201)
        return JsonResponse(serializers.data, status=400)

    if request.method == 'GET':
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return JsonResponse(serializers.data, status=200, safe=False)


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializers = UserSerializer(queryset, many=True)
        return JsonResponse(serializers.data, status=200, safe=False)
