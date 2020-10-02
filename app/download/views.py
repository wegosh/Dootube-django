from django.shortcuts import render, redirect
from django.http import FileResponse

from pytube import YouTube, extract

YOUTUBE_URL = 'https://www.youtube.com/watch?v='

# Create your views here.
def index(request):
    if request.method == "POST":
        video_id = extract.video_id(request.POST.get('ytDownloadUrl'))
        return render(request, 'movieDetails.html', video_id = video_id)
    return render(request, "download.html")

def download(request, video_id):
    return FileResponse(open(YouTube(YOUTUBE_URL + video_id).streams.first().download(skip_existing=True), 'rb'))