from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ipseite.models import Artist, Concert, Festival, Evenement, Ticket, Cart, Order


# Create your views here.
def index(request):
    artists = Artist.objects.all()
    evenements = Evenement.objects.all().order_by('createDate')
    concerts = Concert.objects.all().order_by('date')
    festivals = Festival.objects.all().order_by('startDate')
    return render(request, 'home/index.html',
                  context={"artists": artists, "concerts": concerts, "festivals": festivals, "evenements": evenements})


def event_detail(request, slug):
    event = get_object_or_404(Evenement, slug=slug)
    return render(request, 'home/detail.html', context={"evenement": event})


def add_to_cart(request, slug):
    """ Récupération de l'utilisateur """
    user = request.user
    """ Récupération de l'evenement """
    event = get_object_or_404(Evenement, slug=slug)
    """Récupération ou création du panier """
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, event=event)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("event_detail", kwargs={"slug":slug}))
def ml(request):
    return render(request, 'home/mentionslegales.html')

def concerts(request):
    concerts = Concert.objects.all().order_by('date')
    return render(request, 'home/concerts.html', context={"concerts": concerts})

def festivals(request):
    festivals = Festival.objects.all().order_by('startDate')
    return render(request, 'home/festivals.html', context={"festivals": festivals})

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'home/cart.html', context={"orders":cart.orders.all()})

def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()
    return redirect('index')