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

@login_required(login_url='users:login')
def data(request):
    reservation = Reservation.objects.all().order_by('status')
    context = {'reservation': reservation}
    return render(request, 'admin/data.html', context)

def index(request):
    return render(request, 'sterna.html')


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
        reservation = Reservation(client=request.POST.get('client'), desc=request.POST.get('desc'), start_date=request.POST.get('start_date'), start_time=request.POST.get('start_time'), image=request.FILES.get('image'))

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
        return render(request, 'mypage.html', context)
    else:
        return render(request, 'mypage.html', {'reservation': reservation, 'checked': False})

def new(request):
    return render(request, "new.html")

@login_required(login_url='users:login')
def register(request):
    if request.method == "POST":
        if request.POST.get('completed') =='on':
            completed = 'True'
        else:
            completed = 'False'
        reservation = Reservation(reserv_id=request.POST.get('reserv_id'), client=request.POST.get('client'), desc=request.POST.get('desc'), start_date=request.POST.get('start_date'), start_time=request.POST.get('start_time'), end_date=request.POST.get('start_date'), end_time=request.POST.get('start_time'),top=request.POST.get('top'),bottom=request.POST.get('bottom'),shoes=Shoes.objects.get(id=request.POST['shoes']),location=request.POST.get('location'),cost=request.POST.get('cost'), image=request.FILES.get('image'),status=request.POST.get('status'),completed=completed)

        reservation.save()
        return redirect('reservation:data')
    else:
        form = ReservationForm()
        return render(request, 'admin/register.html', {'form': form})

@login_required(login_url='users:login')
def edit(request, pk):
    return render(request,"admin/edit.html",context)

@login_required(login_url='users:login')
def update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    files = request.FILES
    form = ReservationForm(request.POST, request.FILES, instance=reservation)
    if request.method == "POST":
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.save()
            return redirect('reservation:data')
        else:
            return redirect('reservation:data')
    else:
        form = ReservationForm(instance=reservation)
        return render(request, 'admin/edit.html', {'form': form})