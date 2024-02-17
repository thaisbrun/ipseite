from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from djangoProject import settings
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('mentionslegales', views.ml, name='mentionslegales')
]