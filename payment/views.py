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
    payment = Payment(
        res_obj=reservation,
        reserv_id=reservation.reserv_id,
        name=reservation.client,
        amount=reservation.cost,
    )
    payment.save()

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
    return render(request, "payment/pay_mypage.html", context)


def payment_check(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return redirect("payment_result", pk=payment.pk)


def payment_result(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    reservation = Reservation.objects.filter(reserv_id=payment.reserv_id)
    reservation.update(status="ST3")
    context = {"payment": payment}
    return render(request, "payment/pay_result.html", context)
