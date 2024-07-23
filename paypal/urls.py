from django.urls import path
from . import views

app_name = "paypal"

urlpatterns = [
    path("paypal/", views.paypal, name="paypal"),
    path("paypal/result/<str:pk>/", views.getToken, name="getToken"),
]
