from django.urls import path
from users import views
from rest_framework import viewsets

app_name = 'users'

urlpatterns = [
    path('create/', views.CreateUser.as_view(), name='create'),
]
