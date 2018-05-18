from django.urls import path
from . import views


app_name = 'import_data'

urlpatterns = [
    path('', views.FileUploadView.as_view(), name='import_data'),
    path('<int:pk>/', views.FileUploadViewDetail.as_view(),
         name='import_data_detail'),
]
