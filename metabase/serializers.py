from rest_framework import serializers
from .models import Iframe


class IframeSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Iframe
        fields = ("name", "user", "dashboard")


class IframeSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Iframe
        fields = ("name", "user", "dashboard", "uuid")
