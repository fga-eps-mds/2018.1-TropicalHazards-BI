from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('create/', views.CreateUser.as_view(), name='create'),
    path('index/', views.create_user, name='index'),
    path('', views.UserList.as_view(), name='user-list'),
]
