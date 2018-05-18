import pytest
from django.shortcuts import reverse
from projects.models import Project
from .models import Dashboard
from django.contrib.auth.models import User
from model_mommy import mommy
import json

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
def create_dashboard(client, create_user):
    user = create_user
    project = mommy.make(Project, user=user)
    dashboard = mommy.make(Dashboard, user=user, project=project)
    url = reverse('dashboards:dashboard-detail', kwargs={'pk': dashboard.id})
    return project, dashboard, url


def test_get_dashboard_return_200(client):
    url = reverse('dashboards:dashboards')
    response = client.get(url)

    assert response.status_code == 200


def test_list_dashboards_return_list_dashboards(client):
    url = reverse('dashboards:dashboards')
    dashboard = mommy.make('Dashboard')
    response = client.get(url)

    assert response.data
    assert isinstance(response.data, list)
    assert response.data[0]['name'] == dashboard.name


def test_post_dashboard_is_valid_return_201(client, create_user):
    url = reverse('dashboards:dashboards')
    user = create_user
    project = mommy.make(Project, user=user)
    data = {'user': user.id, 'name': "namedashboard", 'project':
            project.id}

    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")
    assert response.status_code == 201


def test_post_dashboard_is_not_valid_return_400(client, create_user):
    url = reverse('dashboards:dashboards')
    user = create_user
    project = mommy.make(Project, user=user)
    data = {'user': user.id, 'name': " ", 'project':
            project.id}
    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")

    assert response.status_code == 400


def test_post_dashboard_persist_db(client, create_user):
    url = reverse('dashboards:dashboards')
    user = create_user
    project = mommy.make(Project, user=user)
    data = {'user': user.id, 'name': "dashboardname", 'project':
            project.id}
    json_data = json.dumps(data)
    response = client.post(url, data=json_data,
                           content_type="application/json")
    dashboards = Dashboard.objects.all()
    assert response.status_code == 201
    assert dashboards.count() == 1


def test_get_dashboard_detail_return_200(client, create_user,
                                         create_dashboard):
    project, dashboard, url = create_dashboard
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == dashboard.id


def test_get_dashboard_detail_return_404(client, create_user):
    url = reverse('dashboards:dashboard-detail', kwargs={'pk': 1})
    response = client.get(url)

    assert response.status_code == 404


def test_put_dashboard_detail_return_200(client, create_user,
                                         create_dashboard):
    user = create_user
    project, dashboard, url = create_dashboard
    data = {'user': user.id, 'name': "namedashboard", 'project':
            project.id}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')
    assert response.status_code == 200


def test_put_dashboard_detail_return400(client, create_user,
                                        create_dashboard):
    user = create_user
    project, dashboard, url = create_dashboard
    data = {'user': user.id, 'name': " ", 'project':
            project.id}
    json_data = json.dumps(data)
    response = client.put(url, data=json_data, content_type='application/json')

    assert response.status_code == 400


def test_delete_dashboard_detail_return_204(client, create_user,
                                            create_dashboard):
    project, dashboard, url = create_dashboard
    response = client.delete(url, content_type='application/json')

    assert response.status_code == 204
