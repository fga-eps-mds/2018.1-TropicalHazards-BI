from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Modelserializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
