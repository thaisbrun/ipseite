import collections

from django.db import models

# Create your models here.

""" Utilisateur """


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    tel = models.IntegerField(max_length=7)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


""" Commande """


class Order(models.Model):
    quantity = models.IntegerField(max_length=5)
    orderDate = models.DateField()
    totalPrice = models.FloatField(default=0.0)
    deliveryAddress = models.CharField(max_length=100)
    activation = models.BinaryField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listTickets = []


""" Artiste """


class Artist(models.Model):
    name = models.CharField(max_length=70)
    createDate = models.DateField()
    activation = models.BinaryField(default=1)


""" Groupe """


class Band(models.Model):
    name = models.CharField(max_length=70)
    createDate = models.DateField()
    activation = models.BinaryField(default=1)
    listArtists = []


""" Evenement """


class Evenement(models.Model):
    place = models.CharField(100)
    createDate = models.DateField()
    activation = models.BinaryField(default=1)
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

""" Tournée """


class Tour(models.Model):
    name = models.CharField(100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    listConcerts = []


""" Place """


class Ticket(models.Model):
    price = models.FloatField()
    createDate = models.DateField()
    activation = models.BinaryField(default=1)
