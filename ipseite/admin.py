from django.contrib import admin

from ipseite.models import Order, Artist, Band, Evenement, Festival, Concert, Tour, Ticket, Cart, Emplacement

# Register your models here.
admin.site.register(Order)
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Evenement)
admin.site.register(Festival)
admin.site.register(Concert)
admin.site.register(Tour)
admin.site.register(Ticket)
admin.site.register(Cart)
admin.site.register(Emplacement)
