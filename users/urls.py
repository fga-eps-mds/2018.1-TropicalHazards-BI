from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('', views.CreateUser.as_view(), name='create'),
    path('json/', views.create_user, name='json'),
]
