from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='DooTube-index'),
    path('download/<str:video_id>/', download_audio, name='download-audio'),
    path('show_details/<str:video_id>/', movie_details, name="movie-details"),
]