from django.shortcuts import render, redirect
from django.http import FileResponse

from pytube import YouTube, extract

import json

#from dootube_helpers import *


YOUTUBE_URL = 'https://www.youtube.com/watch?v='

# Create your views here.
def index(request):
    if request.method == "POST":
        video_id = extract.video_id(request.POST.get('ytDownloadUrl'))
        if video_id:
            return redirect('movie_details', video_id = video_id)
    return render(request, "download.html")



def movie_details(request, video_id):
    if request.method == "POST":
        #Check if video_id has changed 
        video_id =  extract.video_id(request.POST.get('ytDownloadUrl'))

        if video_id:
            return redirect(movie_details(request, video_id))
    
    youtube_movie_details = YouTube(YOUTUBE_URL + video_id)
    movie_title = youtube_movie_details.title
    movie_thumbnail = youtube_movie_details.thumbnail_url


    return render(request, "download.html")

def download_audio(request, video_id):
    return FileResponse(open(YouTube(YOUTUBE_URL + video_id).streams.first().download(skip_existing=True), 'rb'))