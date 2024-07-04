from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from ckeditor_uploader.fields import RichTextUploadingField


def image_upload_path(instance, filename):
    time=timezone.now()
    return f'{instance}/{filename}'

class Shoes(models.Model):
    name = models.CharField(max_length=50, blank=True)
    amount250 = models.IntegerField(blank=False)
    amount260 = models.IntegerField(blank=False)
    amount270 = models.IntegerField(blank=False)
    amount280 = models.IntegerField(blank=False)
    link = models.URLField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    reserv_id = models.CharField(max_length=20, primary_key=True)
    client = models.CharField(max_length=20)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, default=timezone.now)
    end_date = models.DateField()
    end_time = models.TimeField(blank=True, default=timezone.now)
    top = models.CharField(max_length=50, blank=True)
    bottom = models.CharField(max_length=50, blank=True)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name="shoesName")
    image = models.ImageField(upload_to="", blank=True)
    desc = models.TextField(blank=True, default="-")
    status = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)
    cost = models.IntegerField(default=0)
    location = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.completed)+" " + self.client + "_" + self.reserv_id

