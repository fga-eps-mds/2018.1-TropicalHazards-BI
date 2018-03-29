import pytest
from django.shortcuts import reverse
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db


def test_get_user_return_200(client):
    url = reverse('users:users')
    response = client.get(url)

    assert response.status_code == 200


def test_list_user_return_list_user(client):
    url = reverse('users:users')
    users_create = User.objects.create(username='username',
                                       email='email', password='password')

    response = client.get(url)

    assert response.data
    assert isinstance(response.data, list)
    assert response.data[0]['username'] == users_create.username


def test_post_user_is_valid_return_201(client):
    """ Test valid input create user """
    url = reverse('users:users')
    data = {'username': "username", 'email': "email@email.com",
            'password': "password"}
    response = client.post(url, data=data)

    assert response.status_code == 201


def test_post_user_is_not_valid_return_400(client):
    """ Test not valid input create user """
    url = reverse('users:users')
    data = {'username': "", 'email': "", 'password': '12345678910'}
    response = client.post(url, data=data)

    assert response.status_code == 400


def test_post_user_persist_db(client):
    """ Test persist users in database """
    url = reverse('users:users')
    data = {'username': "username", 'email': "email@email.com",
            'password': "password"}
    client.post(url, data=data)
    users = User.objects.all()

    assert users.count() == 1
