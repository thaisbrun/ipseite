from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ipseite.models import Artist, Concert, Festival, Evenement, Ticket, Cart, Order, Emplacement


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
    emplacements = Emplacement.objects.all()
    festivals = Festival.objects.all()
    concerts = Concert.objects.all()
    ticketLowerPrice = Ticket.objects.all().filter(event=event).order_by('price').first()
    for concert in concerts:
        if event.id == concert.id:
            return render(request, 'home/detail.html', context={"evenement": concert, "emplacements": emplacements,
                                                                "ticketLowerPrice": ticketLowerPrice})
    for festival in festivals:
        if event.id == festival.id:
            return render(request, 'home/detail.html', context={"evenement": festival})


def add_to_cart(request):

    if request.method == "POST":
        """ Récupération de l'utilisateur """
    user = request.user
    """ Récupération de l'evenement """
    event_id = request.POST.get('evenement')
    emplacement_id = request.POST.get('emplacement')
    event = get_object_or_404(Evenement, id=event_id)
    emplacement = get_object_or_404(Emplacement, id=emplacement_id)
    ticket = Ticket.objects.all().filter(event=event, emplacement=emplacement, user__isnull=True).first()
    """Récupération ou création du panier """
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, event=event, ticket=ticket)
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect('index')

#A mettre dans création fonction pour paiement validé :
    #ticket.user = user
   # ticket.save()
def ml(request):
    return render(request, 'home/mentionslegales.html')

def concerts(request):
    concerts = Concert.objects.all().order_by('date')
    tickets = Ticket.objects.all().order_by('createDate')
    for concert in concerts:
            ticketLowerPrice = Ticket.objects.filter(event_id=concert.id).order_by('price').first()
            emplacements = Ticket.objects.filter(event_id=concert.id).order_by('emplacement__name')
            return render(request, 'home/concerts.html', context={"concerts": concerts, "emplacements": emplacements, "ticketLowerPrice": ticketLowerPrice})

def festivals(request):
    festivals = Festival.objects.all().order_by('startDate')
    for festival in festivals:
        ticketLowerPrice = Ticket.objects.filter(event_id=festival.id).order_by('price').first()
    return render(request, 'home/festivals.html', context={"festivals": festivals,
                                                           "ticketLowerPrice": ticketLowerPrice })

def cart(request):
    try:
        cart = Cart.objects.get(id=request.user.cart.id)
    except Cart.DoesNotExist:
        return render(request,'home/cart.html')
    if request.user is not None:
        return render(request, 'home/cart.html', context={"orders": cart.orders.all()})
    else:
        return render(request, 'accounts/login.html')

def delete_orderFromCart(request, id):
    order = Order.objects.get(id=id, user=request.user)
    if order is not None:
        if order.quantity == 1 and order.quantity != 0:
            order.delete()
        else:
            order.quantity -= 1
            order.save()

    return redirect('cart')
def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()
    return redirect('index')

