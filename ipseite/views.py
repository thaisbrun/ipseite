from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from ipseite.models import Artist, Concert, Festival, Evenement, Ticket


# Create your views here.
def index(request):
    artists = Artist.objects.all()
    evenements = Evenement.objects.all()
    concerts = Concert.objects.all()
    festivals = Festival.objects.all()
    return render(request, 'home/index.html',
                  context={"artists": artists, "concerts": concerts, "festivals": festivals, "evenements": evenements})


def event_detail(request, slug):
    event = get_object_or_404(Evenement, slug=slug)
    return render(request, 'home/detail.html', context={"evenement": event})


def add_to_cart(request):
    pass


def ml(request):
    return render(request, 'home/mentionslegales.html')

def concerts(request):
    concerts = Concert.objects.all()
    return render(request, 'home/concerts.html', context={"concerts": concerts})

def festivals(request):
    festivals = Festival.objects.all()
    return render(request, 'home/festivals.html', context={"festivals": festivals})