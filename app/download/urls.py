from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='DooTube-index'),
    path('download/<str:video_id>', views.download, name='download-download'),
]