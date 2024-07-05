from django.urls import path
from . import views

app_name = 'reservation'
urlpatterns = [
    path("", views.index, name="index"),
    path("sterna/book/", views.book, name="book"),
    path("reservation/", views.reservation, name="reservation"),
    path("info/", views.info, name="info"),
    path("sterna/check/", views.check, name='check'),
    path("sterna/contact/", views.contact, name="contact"),
    path("sterna/checked/", views.checked, name="checked"),
    path("ready/", views.ready, name="ready"),
    path("sterna/", views.sterna, name="sterna"),
    path("sterna/mypage/", views.mypage, name="mypage"),
    path("sterna/data/", views.data, name="data"),
    path("sterna/register/", views.register, name="register"),
    path("sterna/edit/<str:pk>", views.edit, name="edit"),
    path('sterna/update/<str:pk>', views.update, name='update'),
]
