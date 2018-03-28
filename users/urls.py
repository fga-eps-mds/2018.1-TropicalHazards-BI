from django.urls import path
from users import views


app_name = 'users'

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
]
