import json
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import requests
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
    return render(request, "EN/sterna.html")


def indexKO(request):
    return render(request, "KO/sterna.html")


def check(request):
    return render(request, "EN/check.html")


def checkKO(request):
    return render(request, "KO/check.html")


def info(request):
    return render(request, "backup/info.html")


def contact(request):
    return render(request, "EN/contact.html")


def contactKO(request):
    return render(request, "KO/contact.html")


def ready(request):
    return render(request, "backup/ready.html")


def sterna(request):
    return render(request, "EN/sterna.html")


def sternaKO(request):
    return render(request, "KO/sterna.html")


def pay(request):
    return render(request, "admin/pay.html")


def policy(request):
    return render(request, "terms/privacy.html")


def cs(request):
    return render(request, "terms/cs.html")


def use(request):
    return render(request, "terms/use.html")


def sizepage(request):
    return render(request, "EN/sizepage.html")


def sizepageKO(request):
    return render(request, "KO/sizepage.html")


def book(request):
    return render(request, "EN/book.html")


def bookKO(request):
    return render(request, "KO/book.html")


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
            request, "EN/mypage.html", {"reservation": reservation, "checked": False}
        )


def checkedKO(request):
    if request.method == "POST":
        checked = request.POST["checked"]
        reservation = Reservation.objects.filter(pk=checked)
        print(checked)
        if len(reservation) == 1:
            results = Reservation.objects.get(pk=checked)
            return redirect("reservation:mypageKO", results.pk)
        elif len(checked) == 0:
            return redirect("reservation:mypageKO", "blank")
        else:
            return redirect("reservation:mypageKO", "noresult")
    else:
        return render(
            request, "KO/mypage.html", {"reservation": reservation, "checked": False}
        )


def mypage(request, pk):
    reservation = Reservation.objects.all()
    if request.method == "GET":
        results = reservation.filter(Q(reserv_id=pk))
        context = {"result_amo": len(results), "checked": pk, "results": results}
        return render(request, "EN/mypage.html", context)
    else:
        return render(
            request, "EN/mypage.html", {"reservation": reservation, "checked": False}
        )


def mypageKO(request, pk):
    reservation = Reservation.objects.all()
    if request.method == "GET":
        results = reservation.filter(Q(reserv_id=pk))
        context = {"result_amo": len(results), "checked": pk, "results": results}
        return render(request, "KO/mypage.html", context)
    else:
        return render(
            request, "KO/mypage.html", {"reservation": reservation, "checked": False}
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
            reserv_id="ste-" + datetime.now().strftime("%Y%m%dT%H%M%S"),
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

        # LINE Notify 액세스 토큰
        line_token = "keAeVnqfCkgFuxZSRBGUwymSN9aqpQC5NXV68GoOVLB"

        # LINE Notify API 엔드포인트 URL
        url = "https://notify-api.line.me/api/notify"

        # 이미지 파일 열기

        # POST 요청 보내기
        response = requests.post(
            url,
            headers={"Authorization": "Bearer " + line_token},
            data={
                "message": "새로운 예약이 접수되었습니다. 예약번호: "
                + str(request.POST.get("reserv_id"))
            },
        )

        # 요청 결과 출력
        print(response.text)

        return redirect("reservation:data")
    else:
        form = ReservationForm()
        return render(request, "admin/register.html", {"form": form})


@login_required(login_url="users:login")
def register2(request):
    if request.method == "POST":

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
            reserv_id="ste-" + datetime.now().strftime("%Y%m%dT%H%M%S"),
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
            image=request.FILES.get("image"),
        )

        reservation.save()

        # LINE Notify 액세스 토큰
        line_token = "keAeVnqfCkgFuxZSRBGUwymSN9aqpQC5NXV68GoOVLB"

        # LINE Notify API 엔드포인트 URL
        url = "https://notify-api.line.me/api/notify"

        # 이미지 파일 열기

        # POST 요청 보내기
        response = requests.post(
            url,
            headers={"Authorization": "Bearer " + line_token},
            data={
                "message": "새로운 예약이 접수되었습니다. 예약번호: "
                + str(request.POST.get("client"))
            },
        )

        # 요청 결과 출력
        print(response.text)

        return redirect("reservation:data")
    else:
        return render(request, "EN/register.html")


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
    if request.method == "GET":
        reservation = Reservation.objects.get(pk=pk)
        reservation.delete()
        return redirect("reservation:data")
    else:
        return redirect("reservation:data")


@login_required(login_url="users:login")
def delpage(request, pk):
    reservation = Reservation.objects.filter(pk=pk)
    return render(request, "admin/delete.html", {"reservation": reservation})
