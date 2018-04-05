import pytest
from django.shortcuts import reverse
from .models import Project
import json 

pytestmark = pytest.mark.django_db


def test_get_project_return_200(client):
    url = reverse('projects:projects')
    response = client.get(url)

    assert response.status_code == 200

def test_list_project_return_list_project(client):
    url = reverse('projects:projects')
    projects_create = Project.objects.create(name='name',
                                       description='description')

    response = client.get(url)

    assert response.data
    assert isinstance(response.data, list)
    assert response.data[0]['name'] == projects_create.name


def test_post_project_is_valid_return_201(client):
    url = reverse('projects:projects')
    data = {'name': "name", 'description': "description"}

    response = client.post(url, data=data)

    assert response.status_code == 201

def test_post_project_is_not_valid_return_400(client):
    url = reverse('projects:projects')
    data = {'name':"", 'description':"description"}
    response = client.post(url, data=data)

    assert response.status_code == 400

# Create your tests here.
