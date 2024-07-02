from django.urls import path
from . import views

app_name = 'reservation'
urlpatterns = [
    path("", views.index, name="index"),
    path("sterna/book/", views.book, name="book"),
    path("reservation/", views.reservation, name="reservation"),
    path("info/", views.info, name="info"),
    path("check/", views.check, name='check'),
    path("contact/", views.contact, name="contact"),
    path("checked/", views.checked, name="checked"),
    path("ready/", views.ready, name="ready"),
    path("sterna/", views.sterna, name="sterna"),
    path("sterna/mypage/", views.mypage, name="mypage"),
]
