from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from datetime import date

from ipseite.models import Artist, Concert, Festival, Evenement, Ticket, Cart, Order, Emplacement


# Create your views here.
def index(request):
    artists = Artist.objects.all()
    evenements = Evenement.objects.all().order_by('createDate').annotate(nombre_tickets=Count('ticket', filter=Q(ticket__user__isnull=True)))
    concerts = Concert.objects.all().order_by('-date','artist__name').annotate(nombre_tickets=Count('ticket', filter=Q(ticket__user__isnull=True)))
    festivals = Festival.objects.all().order_by('startDate').annotate(nombre_tickets=Count('ticket', filter=Q(ticket__user__isnull=True)))
    return render(request, 'home/index.html',
                  context={"artists": artists, "concerts": concerts, "festivals": festivals, "evenements": evenements})


def event_detail(request, slug):
    event = get_object_or_404(Evenement, slug=slug)
    festivals = Festival.objects.all()
    concerts = Concert.objects.all()
    emplacements = Ticket.objects.filter(event=event, user__isnull=True).values('emplacement__name', 'emplacement_id').distinct()
    ticketLowerPrice = Ticket.objects.all().filter(event=event, user__isnull=True).order_by('price').first()
    for concert in concerts:
        if event.id == concert.id:
            return render(request, 'home/detail.html', context={"evenement": concert, "emplacements": emplacements,
                                                                "ticketLowerPrice": ticketLowerPrice})
    for festival in festivals:
        if event.id == festival.id:
            return render(request, 'home/detail.html', context={"evenement": festival, "ticketLowerPrice": ticketLowerPrice})


def add_to_cart(request):

    if request.method == "POST":
        """ Récupération de l'utilisateur """
    user = request.user
    """ Récupération de l'evenement """
    slug = request.POST.get('slug')
    emplacement_id = request.POST.get('emplacement')
    event = get_object_or_404(Evenement, slug=slug)
    emplacement = get_object_or_404(Emplacement, id=emplacement_id)
    ticket = Ticket.objects.all().filter(event=event, emplacement=emplacement, user__isnull=True).first()
    """Récupération ou création du panier """
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, event=event, ticket=ticket)
    order.ticket.user = user
    order.ticket.createDate = date.today()
    order.ticket.save()
    if created:
        order.save()
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect('index')
def ml(request):
    return render(request, 'home/mentionslegales.html')

def concerts(request):
    concerts = Concert.objects.all().order_by('date')

    for concert in concerts:
        emplacements = concert.ticket_set.filter(user__isnull=True).values('emplacement__name').distinct()
        ticketLowerPrice = concert.ticket_set.filter(user__isnull=True).order_by('price').first()

        return render(request, 'home/concerts.html', context={"concerts": concerts,
                                                          'emplacements': emplacements,
                                                          "ticketLowerPrice": ticketLowerPrice})

def festivals(request):
    festivals = Festival.objects.all().order_by('startDate')
    for festival in festivals:
        ticketLowerPrice = Ticket.objects.filter(event=festival, user__isnull=True).order_by('price').first()
    return render(request, 'home/festivals.html', context={"festivals": festivals,
                                                           "ticketLowerPrice": ticketLowerPrice })

def cart(request):
    try:
        cart = Cart.objects.get(id=request.user.cart.id)
        total = sum(order.ticket.price * order.quantity for order in cart.orders.all())
    except Cart.DoesNotExist:
        return render(request,'home/cart.html')
    if request.user is not None:
        return render(request, 'home/cart.html', context={"orders": cart.orders.all(), "total": total})
    else:
        return render(request, 'accounts/login.html')

def add_orderFromCart(request, id):
    user = request.user
    order = get_object_or_404(Order, id=id)
    ticket = Ticket.objects.all().filter(event=order.event, emplacement=order.ticket.emplacement, user__isnull=True).first()
    """Récupération ou création du panier """
    order, created = Order.objects.get_or_create(user=user, ordered=False, event=order.event, ticket=ticket)
    order.ticket.user = user
    order.ticket.createDate = date.today()
    order.ticket.save()
    if order is not None:
        if order.quantity != 0:
            order.quantity += 1
            order.ticket.user = request.user
            order.save()
            return redirect('cart')

def delete_orderFromCart(request, id):
    order = Order.objects.get(id=id, user=request.user)
    if order is not None:
        if order.quantity == 1 and order.quantity != 0:
            order.ticket.user = None
            order.ticket.save()
            order.delete()
        else:
            order.quantity -= 1
            order.ticket.user = None
            order.ticket.save()
            order.save()

    return redirect('cart')
def delete_cart(request):
    if cart := request.user.cart:
       # cart.orders.delete()
        cart.delete()
    return redirect('index')

