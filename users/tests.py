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

    response = client.get(url, content_type="application/json")

    assert response.data
    assert isinstance(response.data, list)
    assert response.data[0]['username'] == users_create.username
