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


def test_post_import_data_user_not_logged(factory, url, mongo_db):
    """ Test post using FileUploadView with no user logged in """

    request = factory.post(url, data={}, format='multipart')

    fileupload = views.FileUploadView()
    response = fileupload.as_view(mongo_db=mongo_db)(request)

    assert response.status_code == 401


def test_post_import_data_user_logged_in(factory, file_csv, url,
                                         project, mongo_db, user,
                                         valid_table_headers):
    """ Test post using FileUploadView with user logged in """

    data = {"file": file_csv, "project": project.id,
            "headers": valid_table_headers}

    request = factory.post(url, data=data, format='multipart')
    force_authenticate(request, user=user)

    fileupload = views.FileUploadView()
    fileupload.mongo_db = mongo_db
    response = fileupload.as_view()(request)

    assert response.status_code == 201


def test_saved_data_throught_post_import_data(factory, file_csv, url,
                                              project, mongo_db, user,
                                              valid_table_headers):
    """ Test saved data throught post using FileUploadView """

    data = {"file": file_csv, "project": project.id,
            "headers": valid_table_headers}

    request = factory.post(url, data=data, format='multipart')
    force_authenticate(request, user=user)

    fileupload = views.FileUploadView()
    fileupload.as_view(mongo_db=mongo_db)(request)

    collection = "collection_{}".format(project.id)

    assert ImportData.objects.all().count() is 1
    assert collection in mongo_db.collection_names()
    assert mongo_db[collection].find_one({'Col1': 1})


def test_return_400_for_wrong_type_file(factory, url, project, mongo_db, user,
                                        valid_table_headers):

    """ Test return of import data when upload a wrong type of file """

    file = SimpleUploadedFile('test.png', b'conent', content_type='image/png')
    data = {"file": file, "project": project.id,
            "headers": valid_table_headers}

    request = factory.post(url, data=data, format='multipart')
    force_authenticate(request, user=user)

    fileupload = views.FileUploadView()
    response = fileupload.as_view(mongo_db=mongo_db)(request)

    assert response.status_code == 400


def test_check_file_type_right_type_import_data(file_csv):
    """ Test check_file_type of FileUploadView for the right type of file """

    fileupload = views.FileUploadView()
    file_type = fileupload.check_file_type(file_csv)

    assert file_type is 'csv'


def test_check_file_type_wrong_type_import_data():
    """ Test check_file_type of FileUploadView for the wrong type of file """

    file = SimpleUploadedFile('test.png', b'conent', content_type='image/png')
    fileupload = views.FileUploadView()
    with pytest.raises(ValidationError):
        fileupload.check_file_type(file)


def test_dataframe_import_data(file_csv, path_csv):
    """ Test create_data_frame of FileUploadView """

    fileupload = views.FileUploadView()
    file_type = fileupload.check_file_type(file_csv)
    fileupload.save_file_tmp(file_csv, path_csv)
    dataframe = fileupload.create_data_frame(path_csv, file_type)

    assert not dataframe.empty
    assert dataframe.Col1[0] == 1
    assert dataframe.Col2[0] == 2
    assert dataframe.Col3[0] == 3


def test_dropped_columns_import_data(factory, file_csv, url,
                                     project, mongo_db, user):
    """ Test columns dropped when post on FileUploadView """

    headers = [
            {"name": "Col1", "type": "int", "selected": True,
                "transform": ""},
            {"name": "Col2", "type": "int", "selected": True,
                "transform": ""},
            {"name": "Col3", "type": "int", "selected": False,
                "transform": ""}
            ]
    headers = json.dumps(headers)

    data = {"file": file_csv, "project": project.id,
            "headers": headers}

    request = factory.post(url, data=data, format='multipart')
    force_authenticate(request, user=user)

    fileupload = views.FileUploadView()
    fileupload.as_view(mongo_db=mongo_db)(request)

    collection = "collection_{}".format(project.id)

    assert ImportData.objects.all().count() is 1
    assert collection in mongo_db.collection_names()
    assert not mongo_db[collection].find_one({'Col3': 3})


def test_bool_column_treatment(factory, url, project, mongo_db, user):
    """ Test conversion of bool columns when saved
    throught post of FileUploadView """

    file = SimpleUploadedFile('test.csv', b"Col1,Col2,Col3\n1,2,3\n0,3,4",
                              content_type='text/csv')

    headers = [
            {"name": "Col1", "type": "bool", "selected": True,
                "transform": "", "true": 1, "false": 0},
            {"name": "Col2", "type": "int", "selected": True,
                "transform": ""},
            {"name": "Col3", "type": "int", "selected": False,
                "transform": ""}
            ]
    headers = json.dumps(headers)

    data = {"file": file, "project": project.id,
            "headers": headers}

    request = factory.post(url, data=data, format='multipart')
    force_authenticate(request, user=user)
    fileupload = views.FileUploadView()
    fileupload.as_view(mongo_db=mongo_db)(request)

    collection = "collection_{}".format(project.id)

    assert ImportData.objects.all().count() is 1
    assert collection in mongo_db.collection_names()
    assert mongo_db[collection].find_one({'Col1': True})
    assert mongo_db[collection].find_one({'Col1': False})


def test_upper_lower_case_treatment(factory, url, project, mongo_db, user):
    """ Test conversion of columns to upper or lower case when saved
    throught post of FileUploadView """

    file = SimpleUploadedFile('test.csv',
                              b"Col1,Col2\nLOWER,upper\nLOWER,upper",
                              content_type='text/csv')

    headers = [
            {"name": "Col1", "type": "str", "selected": True,
                "transform": "lower"},
            {"name": "Col2", "type": "str", "selected": True,
                "transform": "upper"}
            ]
    headers = json.dumps(headers)

    data = {"file": file, "project": project.id,
            "headers": headers}

    request = factory.post(url, data=data, format='multipart')
    force_authenticate(request, user=user)
    fileupload = views.FileUploadView()
    fileupload.as_view(mongo_db=mongo_db)(request)

    collection = "collection_{}".format(project.id)
    assert ImportData.objects.all().count() is 1
    assert collection in mongo_db.collection_names()
    assert mongo_db[collection].find_one({'Col1': 'lower'})
    assert mongo_db[collection].find_one({'Col2': 'UPPER'})


def test_type_conversion_on_columns(factory, url, project, mongo_db,
                                    user, file_csv):
    """ Test type conversion of columns when saved through
    post on FileUploadView"""

    headers = [
            {"name": "Col1", "type": "int64", "selected": True,
                "transform": ""},
            {"name": "Col2", "type": "int64", "selected": True,
                "transform": ""},
            ]
    headers = json.dumps(headers)

    data = {"file": file_csv, "project": project.id,
            "headers": headers}

    request = factory.post(url, data=data, format='multipart')
    force_authenticate(request, user=user)
    fileupload = views.FileUploadView()
    fileupload.as_view(mongo_db=mongo_db)(request)

    collection = "collection_{}".format(project.id)
    assert ImportData.objects.all().count() is 1
    assert collection in mongo_db.collection_names()
    assert isinstance(mongo_db[collection].find_one()['Col1'], int)
    assert isinstance(mongo_db[collection].find_one()['Col2'], int)
