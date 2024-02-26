from django.contrib.auth.base_user import AbstractBaseUser
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages

from accounts.models import Shopper
from ipseite.models import Order

User = get_user_model()

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.warning(request, "Aucun compte n'est associé à ce pseudo et ce mot de passe. Veuillez réessayer.")
    return render(request, 'accounts/login.html')

def my_account(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        User.objects.filter(id=request.user.id).update(first_name=first_name, last_name=last_name, email=email, username=username)
        return redirect('index')
    orders = Order.objects.filter(user=request.user).order_by('-orderDate')[:3]
    total = sum(order.ticket.price * order.quantity for order in orders)

    return render(request,'accounts/my_account.html',context={"orders": orders, "total":total})
def logout_user(request):
    logout(request)
    return redirect('index')

def delete_user(request):
    User.objects.filter(id=request.user.id).delete()
    return redirect('login')