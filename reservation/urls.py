from django.urls import path
from . import views

app_name = "reservation"
urlpatterns = [
    path("", views.index, name="index"),
    path("sterna/book/", views.book, name="book"),
    path("reservation/", views.reservation, name="reservation"),
    path("info/", views.info, name="info"),
    path("sterna/policy/", views.policy, name="policy"),
    path("sterna/cs/", views.cs, name="cs"),
    path("sterna/use/", views.use, name="use"),
    path("sterna/check/", views.check, name="check"),
    path("sterna/contact/", views.contact, name="contact"),
    path("sterna/checked/", views.checked, name="checked"),
    path("sterna/size/", views.sizepage, name="sizepage"),
    path("ready/", views.ready, name="ready"),
    path("sterna/", views.sterna, name="sterna"),
    path("sterna/mypage/<str:pk>", views.mypage, name="mypage"),
    path("sterna/data/", views.data, name="data"),
    path("sterna/register/", views.register, name="register"),
    path("sterna/pay/", views.pay, name="pay"),
    path("sterna/update/<str:pk>", views.update, name="update"),
    path("sterna/delreserv/<str:pk>", views.delreserv, name="delreserv"),
    path("sterna/delpage/<str:pk>", views.delpage, name="delpage"),
]
