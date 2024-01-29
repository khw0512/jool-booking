from django.urls import path
from . import views

app_name = 'reservation'
urlpatterns = [
    path("", views.index, name="index"),
    path("book/", views.book, name="book"),
    path("info/", views.info, name="info"),
    path("check/", views.check, name='check'),
    path("contact/", views.check, name="contact"),
]
