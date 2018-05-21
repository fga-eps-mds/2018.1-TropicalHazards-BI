import pytest
from django.shortcuts import reverse
from model_mommy import mommy
from .models import Tag
from django.contrib.auth.models import User
import json

pytestmark = pytest.mark.django_db


def test_get_tag_return_200(client):
    url = reverse('tags:tags')
    response = client.get(url)

    assert response.status_code == 200


def test_list_tag_return_list_project(client):
    url = reverse('tags:tags')
    tag = mommy.make('Tag')
    response = client.get(url)

    assert response.data
    assert isinstance(response.data, list)
    assert response.data[0]['name'] == tag.name


def test_post_tag_is_valid_return_201(client):
    url = reverse('tags:tags')
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    data = {'name': "tagname", 'slug': "tagslug"}

    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")
    assert response.status_code == 201


def test_post_tag_is_not_valid_return_400(client):
    url = reverse('tags:tags')
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    data = {'name': " ", 'slug': "tagslug"}

    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")

    assert response.status_code == 400


def test_post_tag_persist_db(client):
    url = reverse('tags:tags')
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    data = {'name': "tagname", 'slug': "tagslug"}
    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")
    tags = Tag.objects.all()
    assert response.status_code == 201
    assert tags.count() == 1


def test_get_tag_detail_return_200(client):
    tag = mommy.make('Tag')
    url = reverse('tags:tag-detail', kwargs={'pk': tag.id})
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == tag.id


def test_get_tag_detail_return_404(client):
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    url = reverse('tags:tag-detail', kwargs={'pk': 1})
    response = client.get(url)

    assert response.status_code == 404


def test_put_tag_detail_return_200(client):
    user = User.objects.create(username='username',
                               email='email', is_superuser=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    tag = mommy.make('Tag')
    url = reverse('tags:tag-detail', kwargs={'pk': tag.id})
    data = {'name': "tagname", 'slug': "tagslug"}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')
    assert response.status_code == 200


def test_put_tag_detail_return_401(client):
    user = User.objects.create(username='username',
                               email='email')
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    tag = mommy.make('Tag')
    url = reverse('tags:tag-detail', kwargs={'pk': tag.id})
    data = {'name': "tagname", 'slug': "tagslug"}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')
    assert response.status_code == 401


def test_put_project_detail_return400(client):
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    tag = mommy.make('Tag')
    url = reverse('tags:tag-detail', kwargs={'pk': tag.id})
    data = {'name': "", 'slug': "tagslug"}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')

    assert response.status_code == 400


def test_delete_project_detail_return_204(client):
    user = User.objects.create(username='username',
                               email='email', is_superuser=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    tag = mommy.make('Tag')
    url = reverse('tags:tag-detail', kwargs={'pk': tag.id})
    response = client.delete(url, content_type='application/json')

    assert response.status_code == 204


def test_delete_project_detail_return_401(client):
    user = User.objects.create(username='username',
                               email='email')
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    tag = mommy.make('Tag')
    url = reverse('tags:tag-detail', kwargs={'pk': tag.id})
    response = client.delete(url, content_type='application/json')

    assert response.status_code == 401
