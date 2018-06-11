import json
import pytest
import mongomock

from django.shortcuts import reverse
from django.contrib.auth.models import User
from model_mommy import mommy
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from unittest.mock import patch

from TropicalHazards_BI.utils import connect_mongo
from projects.models import Project
from projects.views import ProjectList

pytestmark = pytest.mark.django_db


@pytest.fixture
def create_user(client):
    user = User.objects.create(username='username',
                               email='email', is_staff=True)
    user.set_password('password')
    user.save()
    client.login(username='username', password='password')
    return user


@pytest.fixture
def create_project(client, create_user):
    user = create_user
    project = mommy.make('Project', user=user)
    url = reverse('projects:project-detail', kwargs={'pk': project.id})
    return project, url


@pytest.fixture
def factory():
    return APIRequestFactory()


@pytest.fixture
def mongo_db():
    """Mock mongo connection with mongomock and the
    view function connect_mongo """
    return connect_mongo(engine=mongomock, host='test', port=0)


@pytest.fixture
def mock_metabase_login():
    """ Mock return of function login_metabase from metabase.utils module"""

    mock_login_patch = patch('metabase.utils.login_metabase')
    mock_login = mock_login_patch.start()
    mock_login.return_value = "tokenofmetabase"


@pytest.fixture
def mock_metabase_get_database():
    """ Mock return of function get_database_id from metabase.utils module"""

    mock_get_db_patch = patch('metabase.utils.get_database_id')
    mock_get_db_id = mock_get_db_patch.start()
    mock_get_db_id.return_value = 1


@pytest.fixture
def mock_metabase_get_table():
    """ Mock return of function get_table_id from metabase.utils module"""

    mock_get_table_patch = patch('metabase.utils.get_table_id')
    mock_table_id = mock_get_table_patch.start()
    mock_table_id.return_value = 1


@pytest.fixture
def mock_metabase_sync_schema():
    """ Mock return of function sync_schema from metabase.utils module"""

    mock_sync_schema_patch = patch('metabase.utils.sync_schema')
    mock_sync_schema = mock_sync_schema_patch.start()
    mock_sync_schema.return_value = True


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


def test_post_project_is_valid_return_201(factory, create_user, mongo_db,
                                          mock_metabase_login,
                                          mock_metabase_get_database,
                                          mock_metabase_get_table,
                                          mock_metabase_sync_schema):

    url = reverse('projects:projects')
    data = {'name': "nameproject", 'description': "description",
            'user': create_user.id, "tags": []}

    request = factory.post(url, data=data)
    force_authenticate(request, user=create_user)

    response = ProjectList.as_view(mongo_db=mongo_db)(request)

    assert response.status_code == 201


def test_post_project_is_not_valid_return_400(factory, create_user, mongo_db,
                                              mock_metabase_login,
                                              mock_metabase_get_database,
                                              mock_metabase_get_table,
                                              mock_metabase_sync_schema):

    url = reverse('projects:projects')
    data = {'description': "description"}

    request = factory.post(url, data=data)
    force_authenticate(request, user=create_user)

    response = ProjectList.as_view(mongo_db=mongo_db)(request)

    assert response.status_code == 400


def test_post_project_persist_db(factory, create_user, mongo_db,
                                 mock_metabase_login,
                                 mock_metabase_get_database,
                                 mock_metabase_get_table,
                                 mock_metabase_sync_schema):

    url = reverse('projects:projects')
    data = {'name': "nameproject", 'description': "description",
            'user': create_user.id, "tags": []}

    request = factory.post(url, data=data)
    force_authenticate(request, user=create_user)

    response = ProjectList.as_view(mongo_db=mongo_db)(request)

    projects = Project.objects.all()
    assert response.status_code == 201
    assert projects.count() == 1


def test_collection_creation_on_post_project(factory, create_user, mongo_db,
                                             mock_metabase_login,
                                             mock_metabase_get_database,
                                             mock_metabase_get_table,
                                             mock_metabase_sync_schema):
    assert Project.objects.all().count() == 0

    url = reverse('projects:projects')
    data = {'name': "nameproject", 'description': "description",
            'user': create_user.id, "tags": []}

    request = factory.post(url, data=data)
    force_authenticate(request, user=create_user)

    ProjectList.as_view(mongo_db=mongo_db)(request)

    project = Project.objects.first()

    assert 'collection_{}'.format(project.id) in mongo_db.collection_names()


def test_get_project_detail_return_200(client, create_project):
    project, url = create_project
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == project.id


def test_get_project_detail_return_404(client, create_user):
    url = reverse('projects:project-detail', kwargs={'pk': 1})
    response = client.get(url)

    assert response.status_code == 404


def test_put_project_detail_return_200(client, create_user, create_project):
    user = create_user
    project, url = create_project
    data = {'name': "nameproject", 'description': "description",
            'user': user.id}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')
    assert response.status_code == 200


def test_put_project_detail_return400(client, create_user, create_project):
    user = create_user
    project, url = create_project
    data = {'name': "", 'description': "description", 'user': user.id}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')

    assert response.status_code == 400


def test_delete_project_detail_return_204(client, create_user, create_project):
    project, url = create_project
    response = client.delete(url, content_type='application/json')

    assert response.status_code == 204
