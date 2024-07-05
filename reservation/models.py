from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from ckeditor_uploader.fields import RichTextUploadingField


def image_upload_path(instance, filename):
    time=timezone.now()
    return f'{instance}/{filename}'

class Shoes(models.Model):
    name = models.CharField(max_length=50, blank=False)
    amount250 = models.IntegerField(blank=False)
    amount260 = models.IntegerField(blank=False)
    amount270 = models.IntegerField(blank=False)
    amount280 = models.IntegerField(blank=False)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Top(models.Model):
    name = models.CharField(max_length=50, blank=False)
    amount_s = models.IntegerField(blank=False)
    amount_m = models.IntegerField(blank=False)
    amount_L = models.IntegerField(blank=False)
    amount_XL = models.IntegerField(blank=False)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Bottom(models.Model):
    name = models.CharField(max_length=50, blank=False)
    amount_s = models.IntegerField(blank=False)
    amount_m = models.IntegerField(blank=False)
    amount_L = models.IntegerField(blank=False)
    amount_XL = models.IntegerField(blank=False)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):

    STATUS_CHOICE = [
        ('ST1','예약 양식 제출 완료'),
        ('ST2','예약 완료 및 결제 대기'),
        ('ST3','결제 완료'),
        ('ST4','배송 중'),
        ('ST5','배송 완료'),
        ('ST6','반납 완료'),
        ('ST7','입고 완료')
    ]

    reserv_id = models.CharField(max_length=20, primary_key=True)
    client = models.CharField(max_length=20)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, default=timezone.now)
    end_date = models.DateField()
    end_time = models.TimeField(blank=True, default=timezone.now)
    top = models.ForeignKey(Top, on_delete=models.CASCADE, related_name="topName", blank=True)
    bottom = models.ForeignKey(Bottom, on_delete=models.CASCADE, related_name="bottomName", blank=True)
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE, related_name="shoesName", blank=True)
    image = models.ImageField(upload_to="", blank=True)
    desc = models.TextField(blank=True, default="-")
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICE,
        default='ST1',
    )
    completed = models.BooleanField(default=False)
    cost = models.IntegerField(default=0)
    location = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return str(self.completed)+" " + self.client + "_" + self.reserv_id

