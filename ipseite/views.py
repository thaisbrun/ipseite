from django.shortcuts import render
from django.http import HttpResponse
from ipseite.models import Artist
# Create your views here.
def index(request):
    artists = Artist.objects.all()

    return render(request, 'home/index.html', context={"artists": artists})