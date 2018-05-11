import pytest
from django.shortcuts import reverse
from django.contrib.auth.models import User
from model_mommy import mommy
import json

pytestmark = pytest.mark.django_db


def test_get_project_return_200(client):
    url = reverse('import_data:import_data')
    response = client.get(url)

    assert response.status_code == 200


@pytest.fixture(scope='session')
def test_post_project_is_valid_return_201(client, tmpdir_factory):
    url = reverse('projects:projects')
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')

    file = tmpdir_factory.mktemp('temp').join('test.csv')
    project = mommy.make('Project')

    data = {'file': file, 'project': project}

    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")
    assert response.status_code == 201
