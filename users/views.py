from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, generics
from users.serializers import UserSerializer
 


def create_user(request):
    if resquest.method == 'GET':
        users = User.object.all()
        serializers = UserSerializer(users, many=True)
        return JsonResponse(serializers.data, status=200, safe=False)
    if resquest.method == 'POST':
        data = JSONParser().parse(request)
        serializers = UserSerializer(data = data)
        if serializers.is_valid():
            serializers.save
            return JsonResponse(serializers.data, status=201)
        else:
            return JsonResponse(serializers.data, status=400)

class CreateUser(generics.CreateAPIView):
    serializer_class = UserSerializer
