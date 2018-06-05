import pytest
import json
import os
import mongomock

from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.exceptions import ValidationError
from model_mommy import mommy

from import_data import views
from import_data.models import ImportData

pytestmark = pytest.mark.django_db


@pytest.fixture
def file_csv():
    file = SimpleUploadedFile('test.csv', b"Col1,Col2,Col3\n1,2,3",
                              content_type='text/csv')
    return file


@pytest.fixture
def user(client):
    user = User.objects.create_user(username="username",
                                    email="email@email.com",
                                    password="password")
    return user


@pytest.fixture
def project(user):
    project = mommy.make('Project', user=user)
    return project


@pytest.fixture
def url():
    return reverse('import_data:import_data')


@pytest.fixture
def factory():
    """Mocking APIRequestFactory obj"""
    return APIRequestFactory()


@pytest.fixture
def mongo_db():
    """Mock mongo connection with mongomock and the
    view function connect_mongo """
    return views.connect_mongo(engine=mongomock, host='test', port=0)


@pytest.fixture
def path_csv(file_csv):
    return "tmp/{}".format(file_csv.name)


@pytest.fixture
def valid_table_headers():
    table_headers = [
            {"name": "Col1", "type": "int", "selected": True,
                "transform": ""},
            {"name": "Col2", "type": "int", "selected": True,
                "transform": ""},
            {"name": "Col3", "type": "int", "selected": True,
                "transform": ""}
            ]
    return json.dumps(table_headers)


def teardown_file():
    try:
        os.remove('tmp/test.csv')
    except FileNotFoundError:
        pass


def test_save_file_import_data(factory, file_csv, path_csv):
    fileupload = views.FileUploadView()
    fileupload.save_file_tmp(file=file_csv, file_path=path_csv)
    file = open("tmp/test.csv", "r")

    assert file.read() is not None
    teardown_file()


def test_fail_result_for_save_mongo(mongo_db):
    """ Test return when save on mongo fails """

    fileupload = views.FileUploadView()
    fileupload.mongo_db = mongo_db

    data = {}
    project_id = 0

    result = fileupload.save_on_mongo(data, project_id)

    assert result is False


def test_result_sucess_for_save_mongo(mongo_db):
    """ Test return when save on mongo succeed"""
    fileupload = views.FileUploadView()
    fileupload.mongo_db = mongo_db

    data = [dict(data=1)]
    project_id = 1
    result = fileupload.save_on_mongo(data, project_id)

    assert result is True
    assert 'collection_1' in mongo_db.collection_names()
    assert mongo_db['collection_1'].find_one({'data': 1})

