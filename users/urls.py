from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    #path('', views.CreateUser.as_view(), name='create'),
    path('list/', views.UserList.as_view()),
    path('list/<int:pk>/', views.UserDetail.as_view()),
]
