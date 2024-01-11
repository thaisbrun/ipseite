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

""" Evenement """

class Evenement(models.Model):
    place = models.CharField(max_length=100)
    slug = models.SlugField(max_length=70)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
    image = models.ImageField(upload_to="imagesEv", blank=True, null=True)
    nbTickets = models.IntegerField(default=1)

""" Emplacement """
class Emplacement(models.Model):
    name = models.CharField(max_length=40)
    dateCreation = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

""" Ticket """
class Ticket(models.Model):
    price = models.FloatField(default=0.0)
    emplacement = models.ForeignKey(Emplacement, on_delete=models.CASCADE)
    createDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE)

""" Festival """
class Festival(Evenement):
    startDate = models.DateField(default=timezone.now)
    finishDate = models.DateField(default=timezone.now)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    artists = models.ManyToManyField(Artist)

""" Concert """

class Concert(Evenement):
    date = models.DateField(default=timezone.now)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)


""" Commande """

class Order(models.Model):
    quantity = models.IntegerField(default=1)
    totalPrice = models.FloatField(default=0.0)
    ordered = models.BooleanField(default=False)
    orderDate = models.DateField(default=timezone.now)
    activation = models.BinaryField()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event.place} ({self.quantity})"


""" Panier """

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)