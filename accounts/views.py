from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

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
    return render(request, 'accounts/login.html')

def my_account(request):
        orders = Order.objects.filter(User.objects.get("user_id"))
        return render(request,'accounts/my_account.html', context={"orders":orders})
def logout_user(request):
    logout(request)
    return redirect('index')
