from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from djangoProject import settings
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('mentionslegales', views.ml, name='mentionslegales')
]