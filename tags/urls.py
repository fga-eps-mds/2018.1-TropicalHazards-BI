from django.urls import path
from . import views


app_name = 'tags'

urlpatterns = [
    path('', views.TagList.as_view(), name='tags'),
    path('<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
]
