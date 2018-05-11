# import pytest
# from django.shortcuts import reverse
# from django.contrib.auth.models import User
# from model_mommy import mommy
# from django.core.files.uploadedfile import SimpleUploadedFile
# # import json

# pytestmark = pytest.mark.django_db


# def test_post_data_import_is_valid_return_201(client):
#     url = reverse('import_data:import_data')
#     user = User.objects.create(username='username',
#                                email='email', is_staff=True)
#     user.set_password('password')
#     user.save()
#     client.login(username='username', password='password')

#     file = SimpleUploadedFile('test.csv', b" test ", content_type='text/csv')
#     project = mommy.make('Project')

#     response = client.post(url, data={'file': file, 'project': project.id})
#     assert response.status_code == 201
