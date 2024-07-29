from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Max
from django.db.models import Q
from django.core.paginator import Paginator
from django.core import serializers
from .forms import ReservationForm
from django.contrib.auth.models import User
import os


@login_required(login_url="users:login")
def data(request):
    reservation = Reservation.objects.all().order_by("status")
    context = {"reservation": reservation}
    return render(request, "admin/data.html", context)


def index(request):
    return render(request, "sterna.html")


def check(request):
    return render(request, "check.html")


def info(request):
    return render(request, "info.html")


def contact(request):
    return render(request, "contact.html")


def reservation(request):
    return render(request, "book.html")


def ready(request):
    return render(request, "ready.html")


def sterna(request):
    return render(request, "sterna.html")


def pay(request):
    return render(request, "admin/pay.html")


def policy(request):
    return render(request, "terms/privacy.html")


def cs(request):
    return render(request, "terms/cs.html")


def use(request):
    return render(request, "terms/use.html")


def sizepage(request):
    return render(request, "sizepage.html")


def book(request):
    if request.method == "POST":
        reservation = Reservation(
            client=request.POST.get("client"),
            desc=request.POST.get("desc"),
            start_date=request.POST.get("start_date"),
            start_time=request.POST.get("start_time"),
            image=request.FILES.get("image"),
        )

        reservation.save()
        return render(request, "index.html")
    else:
        form = ReservationForm()
        return render(request, "book.html", {"form": form})


def checked(request):
    if request.method == "POST":
        checked = request.POST["checked"]
        reservation = Reservation.objects.filter(pk=checked)
        print(checked)
        if len(reservation) == 1:
            results = Reservation.objects.get(pk=checked)
            return redirect("reservation:mypage", results.pk)
        elif len(checked) == 0:
            return redirect("reservation:mypage", "blank")
        else:
            return redirect("reservation:mypage", "noresult")
    else:
        return render(
            request, "mypage.html", {"reservation": reservation, "checked": False}
        )


def mypage(request, pk):
    reservation = Reservation.objects.all()
    if request.method == "GET":
        results = reservation.filter(Q(reserv_id=pk))
        context = {"result_amo": len(results), "checked": pk, "results": results}
        return render(request, "mypage.html", context)
    else:
        return render(
            request, "mypage.html", {"reservation": reservation, "checked": False}
        )


def new(request):
    return render(request, "new.html")


@login_required(login_url="users:login")
def register(request):
    if request.method == "POST":
        if request.POST.get("completed") == "on":
            completed = "True"
        else:
            completed = "False"

        if Item.objects.filter(pk=request.POST.get("top")).exists():
            top = Item.objects.get(pk=request.POST.get("top"))
        else:
            top = None

        if Item.objects.filter(pk=request.POST.get("bottom")).exists():
            bottom = Item.objects.get(pk=request.POST.get("bottom"))
        else:
            bottom = None

        if Item.objects.filter(pk=request.POST.get("shoes")).exists():
            shoes = Item.objects.get(pk=request.POST.get("shoes"))
        else:
            shoes = None

        if Item.objects.filter(pk=request.POST.get("bag")).exists():
            bag = Item.objects.get(pk=request.POST.get("bag"))
        else:
            bag = None

        reservation = Reservation(
            reserv_id=request.POST.get("reserv_id"),
            client=request.POST.get("client"),
            contact=request.POST.get("contact"),
            desc=request.POST.get("desc"),
            start_date=request.POST.get("start_date"),
            start_time=request.POST.get("start_time"),
            end_date=request.POST.get("end_date"),
            end_time=request.POST.get("end_time"),
            top=top,
            bottom=bottom,
            shoes=shoes,
            bag=bag,
            location=request.POST.get("location"),
            cost=request.POST.get("cost"),
            image=request.FILES.get("image"),
            status=request.POST.get("status"),
            paypal_link=request.POST.get("paypal_link"),
            completed=completed,
        )

        reservation.save()
        return redirect("reservation:data")
    else:
        form = ReservationForm()
        return render(request, "admin/register.html", {"form": form})


@login_required(login_url="users:login")
def update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    form = ReservationForm(request.POST, request.FILES, instance=reservation)
    if request.method == "POST":
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect("reservation:data")
        else:
            return redirect("reservation:data")
    else:
        form = ReservationForm(instance=reservation)
        return render(request, "admin/edit.html", {"form": form})


@login_required(login_url="users:login")
def delreserv(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.delete()
    return redirect("reservation:data")


@login_required(login_url="users:login")
def delpage(request, pk):
    reservation = Reservation.objects.filter(pk=pk)
    print(reservation)
    return render(request, "admin/delete.html", {"reservation": reservation})
