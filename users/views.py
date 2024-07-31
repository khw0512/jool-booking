from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.forms import UserForm
from reservation.models import Reservation

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # stuffs = Stuff()
            # thisCart=Cart(user=user,stuffs=stuffs)
            # thisCart.save()
            # thisCart.user.add(request.user)
            return render(request, "EN/sterna.html")
    else:
        form = UserForm()
    return render(request, "users/signup.html", {"form": form})
