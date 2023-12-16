import collections
import datetime
from django.utils import timezone
from django.db import models

from djangoProject.settings import AUTH_USER_MODEL

# Create your models here.

""" Artiste """


class Artist(models.Model):
    name = models.CharField(max_length=70)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()

    def __str__(self):
        return self.name


""" Groupe """


class Band(models.Model):
    name = models.CharField(max_length=70)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
    artists = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name


""" Tournée """


class Tour(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name




""" Ticket """

class Ticket(models.Model):
    price = models.FloatField(default=0.0)
    emplacement = models.CharField(max_length=50)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()

""" Evenement """

class Evenement(models.Model):
    place = models.CharField(max_length=100)
    slug = models.SlugField(max_length=70)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
    image = models.ImageField(upload_to="imagesEv", blank=True, null=True)
    tickets = models.ManyToManyField(Ticket)

""" Festival """


class Festival(Evenement):
    startDate = models.DateField()
    finishDate = models.DateField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    artists = models.ManyToManyField(Artist)


""" Concert """


class Concert(Evenement):
    date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)


""" Commande """


class Order(models.Model):
    quantity = models.IntegerField(default=1)
    totalPrice = models.FloatField(default=0.0)
    deliveryAddress = models.CharField(max_length=100)
    ordered = models.BooleanField(default=True)
    activation = models.BinaryField()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.place} ({self.quantity})"


""" Panier """


class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    orderDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
