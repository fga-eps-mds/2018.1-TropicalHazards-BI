from django.urls import path
from . import views

app_name = 'dashboards'

urlpatterns = [
    path('', views.DashboardList.as_view(), name='dashboards'),
    path('<int:pk>/', views.DashboardDetail.as_view(),
         name='dashboard-detail'),
    ]
