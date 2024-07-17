from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db.models import Q

from reservation.models import Reservation
from .models import *


def payment(request):
    return render(request, "payment/pay_test.html")


def payment_pay(request, pk):

    print(pk)
    reservation = Reservation.objects.get(pk=pk)
    print(reservation.pk)
    payment = Payment(name=reservation.client, amount=reservation.cost)
    payment.save()
    print(payment)

    results = reservation
    pk = payment.pk

    context = {
        "result_amo": 2,
        "checked": reservation.pk,
        "results": [results],
        "amount": reservation.cost,
        "payment": payment,
        "pk": pk,
    }
    print(context)
    return render(request, "payment/pay_mypage.html", context)


def payment_check(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return redirect("payment_result", pk=payment.pk)


def payment_result(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    print(payment)
    context = {"payment": payment}
    return render(request, "payment/pay_result.html", context)
