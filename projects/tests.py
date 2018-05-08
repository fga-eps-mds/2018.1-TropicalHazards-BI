import pytest
from django.shortcuts import reverse
from .models import Project
from tags.models import Tag
from django.contrib.auth.models import User
from model_mommy import mommy
import json

pytestmark = pytest.mark.django_db


def test_get_project_return_200(client):
    url = reverse('projects:projects')
    response = client.get(url)

    assert response.status_code == 200


def test_list_project_return_list_project(client):
    url = reverse('projects:projects')
    project = mommy.make('Project')
    response = client.get(url)

    assert response.data
    assert isinstance(response.data, list)
    assert response.data[0]['name'] == project.name


def test_post_project_is_valid_return_201(client):
    url = reverse('projects:projects')
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    data = {'name': "nameproject", 'description': "description"}

    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")
    assert response.status_code == 201


def test_post_project_is_not_valid_return_400(client):
    url = reverse('projects:projects')
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    data = {'name': " ", 'description': "description"}
    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")

    assert response.status_code == 400


def test_post_project_persist_db(client):
    url = reverse('projects:projects')
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    data = {'name': "nameproject", 'description': "description"}
    client.login(username='username', password='password')
    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")
    projects = Project.objects.all()
    assert response.status_code == 201
    assert projects.count() == 1


def test_get_project_detail_return_200(client):
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    project = mommy.make('Project', user=user)
    url = reverse('projects:projects-detail', kwargs={'pk': project.id})
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == project.id


def test_get_project_detail_return_404(client):
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')

    url = reverse('projects:projects-detail', kwargs={'pk': 1})
    response = client.get(url)

    assert response.status_code == 404


def test_put_project_detail_return_200(client):
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    project = mommy.make('Project', user=user)
    url = reverse('projects:projects-detail', kwargs={'pk': project.id})
    data = {'name': "nameproject", 'description': "description",
            'user': user.id}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')
    assert response.status_code == 200


def test_put_project_detail_return400(client):
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    project = mommy.make('Project', user=user)
    url = reverse('projects:projects-detail', kwargs={'pk': project.id})
    data = {'name': "", 'description': "description", 'user': user.id}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')

    assert response.status_code == 400


def test_delete_project_detail_return_204(client):
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    project = mommy.make('Project', user=user)
    url = reverse('projects:projects-detail', kwargs={'pk': project.id})
    response = client.delete(url, content_type='application/json')

    assert response.status_code == 204
