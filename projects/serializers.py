from rest_framework import serializers
from .models import Project
from tags.serializers import TagSerializer
from tags.models import Tag


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Project
        fields = ('id', 'user', 'name', 'description', 'tags', 'table_id')

    def create(self, validated_data):
        tag_data = validated_data.pop('tags')
        project = Project.objects.create(**validated_data)

        for tag in tag_data:
            tag, created = Tag.objects.get_or_create(name=tag['name'],
                                                     slug=tag['slug'])
            project.tags.add(tag)
        return project
