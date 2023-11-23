import collections
import datetime
from django.utils import timezone
from django.db import models
# Create your models here.



""" Commande """


class Order(models.Model):
    quantity = models.IntegerField()
    orderDate = models.DateField()
    totalPrice = models.FloatField(default=0.0)
    deliveryAddress = models.CharField(max_length=100)
    activation = models.BinaryField()
    """user = models.ForeignKey(User, on_delete=models.CASCADE)"""
    listTickets = []


""" Artiste """


class Artist(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
    def __str__(self):
       return self.name;


""" Groupe """


class Band(models.Model):
    name = models.CharField(max_length=70)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
    listArtists = []
    def __str__(self):
       return self.name;

""" Tournée """


class Tour(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    listConcerts = []
    def __str__(self):
       return self.name;

""" Evenement """


class Evenement(models.Model):
    place = models.CharField(max_length=100)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
    image = models.ImageField(upload_to="imagesEv", blank=True, null=True)
    listTickets = []

""" Festival """


class Festival(Evenement):
    startDate = models.DateField()
    finishDate = models.DateField()
    listArtists = []

""" Concert """


class Concert(Evenement):
    date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

""" Place """

class Ticket(models.Model):
    price = models.FloatField(default=0.0)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
