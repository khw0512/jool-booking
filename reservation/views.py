from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime, timedelta
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Max
from django.db.models import Q
from django.core.paginator import Paginator
from django.core import serializers
from .forms import ReservationForm


def index(request):
    return render(request, 'index.html')


def check(request):
    return render(request, 'check.html')


def info(request):
    return render(request, 'info.html')


def contact(request):
    return render(request, 'contact.html')


def reservation(request):
    return render(request, 'book.html')


def ready(request):
    return render(request, 'ready.html')


def sterna(request):
    return render(request, 'sterna.html')


def mypage(request):
    return render(request, 'mypage.html')


def book(request):
    if request.method == "POST":
        reservation = Reservation(client=request.POST.get('client'), month=request.POST.get(
            'month'), desc=request.POST.get('desc'), day=request.POST.get('day'), hour=request.POST.get('hour'),
            minute=request.POST.get('minute'), date=request.POST.get('date'), time=request.POST.get('time'))

        reservation.save()
        return render(request, 'index.html')
    else:
        form = ReservationForm()
        return render(request, 'book.html', {'form': form})


def checked(request):
    reservation = Reservation.objects.all()
    if request.method == 'POST':
        checked = request.POST['checked']
        results = reservation.filter(
            Q(reserv_id=checked))
        context = {'result_amo': len(
            results), 'checked': checked, 'results': results}
        print(context)
        return render(request, 'checked.html', context)
    else:
        return render(request, 'checked.html', {'reservation': reservation, 'checked': False})
