from django.shortcuts import render
from django.http import HttpResponse
from ipseite.models import Artist, Concert


# Create your views here.
def index(request):
    artists = Artist.objects.all()
    concerts = Concert.objects.all()
    return render(request, 'home/index.html', context={"artists": artists, "concerts": concerts})