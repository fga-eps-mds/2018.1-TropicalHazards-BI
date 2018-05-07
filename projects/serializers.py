from rest_framework import serializers
from .models import Project
from tags.serializers import TagSerializer


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = ('id', 'user', 'name', 'description', 'tags')

    def create(self, validated_data):
        tag_data = validated_data.pop('tags')
        project = Project.objects.create(**validated_data)
        Tag.objects.create(project=project, **tag_data)
        return project
