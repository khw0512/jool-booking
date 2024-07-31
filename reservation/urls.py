from django.urls import path
from . import views

app_name = "reservation"
urlpatterns = [
    path("", views.index, name="index"),
    path("reservation/", views.reservation, name="reservation"),
    path("info/", views.info, name="info"),
    path("EN/", views.sterna, name="sterna"),
    path("KO/", views.sternaKO, name="sternaKO"),
    path("EN/policy/", views.policy, name="policy"),
    path("EN/cs/", views.cs, name="cs"),
    path("EN/use/", views.use, name="use"),
    path("EN/book/", views.book, name="book"),
    path("KO/book/", views.bookKO, name="bookKO"),
    path("EN/check/", views.check, name="check"),
    path("KO/check/", views.checkKO, name="checkKO"),
    path("EN/contact/", views.contact, name="contact"),
    path("EN/checked/", views.checked, name="checked"),
    path("EN/size/", views.sizepage, name="sizepage"),
    path("ready/", views.ready, name="ready"),
    path("EN/mypage/<str:pk>", views.mypage, name="mypage"),
    path("EN/data/", views.data, name="data"),
    path("EN/register/", views.register, name="register"),
    path("EN/pay/", views.pay, name="pay"),
    path("EN/update/<str:pk>", views.update, name="update"),
    path("EN/delreserv/<str:pk>", views.delreserv, name="delreserv"),
    path("EN/delpage/<str:pk>", views.delpage, name="delpage"),
]
