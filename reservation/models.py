from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from ckeditor_uploader.fields import RichTextUploadingField


def image_upload_path(instance, filename):
    return f'{instance}/{filename}'


class Reservation(models.Model):
    reserv_id = models.CharField(max_length=20, default="HaveToMod!!")
    client = models.CharField(max_length=20)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    top = models.CharField(max_length=50)
    bottom = models.CharField(max_length=50)
    shoes = models.CharField(max_length=50)
    image = models.ImageField(upload_to="", blank=True)
    desc = models.TextField()
    status = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.completed)+" " + self.client + "_" + self.reserv_id
