from django.urls import path
from . import views

app_name = "reservation"
urlpatterns = [
    path("", views.index, name="index"),
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
    path("KO/contact/", views.contactKO, name="contactKO"),
    path("EN/checked/", views.checked, name="checked"),
    path("KO/checked/", views.checkedKO, name="checkedKO"),
    path("EN/size/", views.sizepage, name="sizepage"),
    path("KO/size/", views.sizepageKO, name="sizepageKO"),
    path("ready/", views.ready, name="ready"),
    path("EN/mypage/<str:pk>", views.mypage, name="mypage"),
    path("KO/mypage/<str:pk>", views.mypageKO, name="mypageKO"),
    path("data/", views.data, name="data"),
    path("EN/register/", views.register, name="register"),
    path("EN/register2/", views.register2, name="register2"),
    path("EN/pay/", views.pay, name="pay"),
    path("EN/update/<str:pk>", views.update, name="update"),
    path("EN/delreserv/<str:pk>", views.delreserv, name="delreserv"),
    path("EN/delpage/<str:pk>", views.delpage, name="delpage"),
]
