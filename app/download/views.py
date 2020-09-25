from django.shortcuts import render
from django.http import FileResponse

from pytube import YouTube

# Create your views here.
def index(request):
    if request.method == "POST":
        video_id = get_video_id(request.form['ytDownloadUrl'])
    return render(request, "download.html")

def download(request, video_id):
    return FileResponse(open(Youtube(url).streams.first().download(skip_existing=True), 'rb'))