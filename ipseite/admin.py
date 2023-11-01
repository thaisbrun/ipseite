from django.contrib import admin

from ipseite.models import User, Order, Artist, Band, Evenement, Festival, Concert, Tour, Ticket

# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Evenement)
admin.site.register(Concert)
admin.site.register(Tour)
admin.site.register(Ticket)
