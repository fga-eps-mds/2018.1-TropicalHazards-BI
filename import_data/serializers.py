from rest_framework import serializers
from .models import ImportData


class ImportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportData
        fields = ('last_modified', 'project')
