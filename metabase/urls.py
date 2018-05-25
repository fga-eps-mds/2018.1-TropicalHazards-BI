from django.urls import path
from . import views

app_name = 'iframes'

urlpatterns = [
    path("", views.DashboardIframes.as_view(),
         name='dashboard-iframes'),
]
