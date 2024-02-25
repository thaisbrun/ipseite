from django.urls import path

from . import views

urlpatterns = [
    path('home', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view()),  # new
    path('cancelled/', views.CancelledView.as_view()),  # new
]