from django.urls import path
from . import views

app_name = "paypal"

urlpatterns = [
    path("", views.paypal, name="paypal"),
    path("result/<str:pk>/", views.payment, name="payment"),
    path("check-payment/<str:pk>/", views.checkPayment, name="checkPayment"),
]
