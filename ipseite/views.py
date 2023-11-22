from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ipseite.models import Artist, Concert


# Create your views here.
def index(request):
    artists = Artist.objects.all()
    concerts = Concert.objects.all()
    return render(request, 'home/index.html', context={"artists": artists, "concerts": concerts})


def artist_detail(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    return render(request, 'home/detail.html', context={"artist":artist});
