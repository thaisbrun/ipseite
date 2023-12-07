from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ipseite.models import Artist, Concert, Festival


# Create your views here.
def index(request):
    artists = Artist.objects.all()
    concerts = Concert.objects.all()
    festivals = Festival.objects.all()
    return render(request, 'home/index.html', context={"artists": artists, "concerts": concerts, "festivals":festivals})

def artist_detail(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    return render(request, 'home/detail.html', context={"artist":artist});

def add_to_cart(request):
    pass

def ml(request):
    return render(request, 'home/mentionslegales.html')