import django_filters
from .models import Project


class ProjectFilter(django_filters.FilterSet):
    tag_name = django_filters.CharFilter(name='tags__name')

    class Meta:
        model = Project
        fields = ['tags']
