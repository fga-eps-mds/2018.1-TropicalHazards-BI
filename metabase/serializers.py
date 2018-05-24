from rest_framework import serializers
from .models import Iframe


class IframeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iframe
        fields = ("name", "user", "dashboard", "uuid")
