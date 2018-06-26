from django.urls import path
from . import views

app_name = 'iframes'

urlpatterns = [
        path("<int:pk>", views.DashboardIframes.as_view(),
             name='dashboard-iframes'),
        path("<int:pk>/fields", views.DashboardFields.as_view(),
             name='dashboard-fields')

]
