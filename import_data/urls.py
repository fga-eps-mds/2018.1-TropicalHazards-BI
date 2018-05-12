from django.urls import path
from . import views


app_name = 'import_data'

urlpatterns = [
    path('', views.FileUploadView.as_view(), name='import_data')
]
