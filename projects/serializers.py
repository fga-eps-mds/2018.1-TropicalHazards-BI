from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description')

        def create(self, validated_data):
            project = Project(
                name=validated_data['name'],
                description=validated_data['description'])
            
            project.save()
            return project

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            
            instance.save()
            return instance