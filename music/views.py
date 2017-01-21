from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context) #bydefault django will look for this file inside templates directory

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album: " + str(album_id) + "</h2>")
