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
    data = {'name': "", 'description': "description"}
    response = client.post(url, data=data)

    assert response.status_code == 400


def test_post_project_persist_db(client):
    url = reverse('projects:projects')
    data = {'name': "name", 'description': "description"}
    client.post(url, data=data)

    projects = Project.objects.all()

    assert projects.count() == 1
# Create your tests here.


def test_get_project_detail_return_200(client):

    project = Project.objects.create(name='name', description='description')
    url = reverse('projects:projects-detail', kwargs={'pk': project.id})
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == project.id


def test_get_project_detail_return_404(client):

    url = reverse('projects:projects-detail', kwargs={'pk': 1})
    response = client.get(url)

    assert response.status_code == 404


def test_put_project_detail_return_200(client):
    project = Project.objects.create(name='name', description='description')
    project.save()
    url = reverse('projects:projects-detail', kwargs={'pk': project.id})
    data = {'name': "name", 'description': "description"}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')
    assert response.status_code == 200


def test_put_project_detail_return400(client):
    project = Project.objects.create(name='name', description='description')
    project.save()
    url = reverse('projects:projects-detail', kwargs={'pk': project.id})
    data = {'name': "", 'description': "description"}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')

    assert response.status_code == 400


def test_delete_project_detail_return_204(client):
    project = Project.objects.create(name='name', description='description')
    project.save()
    url = reverse('projects:projects-detail', kwargs={'pk': project.id})
    response = client.delete(url, content_type='application/json')

    assert response.status_code == 204
