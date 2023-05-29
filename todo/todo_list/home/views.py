from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, "index.html", {})



def register(request):
    return render(request, "register.html", {})



def login_user(request):
    if request.method == "POST":
        nickname = request.POST['nickname']
        password = request.POST['password']

        user = authenticate(request, username=nickname, password=password)

        if user is not None:
            login(request, user)
            return redirect("website:home")

        else:
            return redirect("website:login")

    else:
        return render(request, "login.html", {})