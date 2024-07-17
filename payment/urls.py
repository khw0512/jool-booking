from django.urls import path
from . import views

app_name = "payment"

urlpatterns = [
    path("payment/", views.payment, name="payment"),
    path("payment/<str:pk>/", views.payment_pay, name="payment_pay"),
    path("payment/<str:pk>/result", views.payment_result, name="payment_result"),
    path("payment/<str:pk>/check", views.payment_check, name="payment_check"),
]
