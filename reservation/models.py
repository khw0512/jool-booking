from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


def image_upload_path(instance, filename):
    return f'{instance}/{filename}'


class Reservation(models.Model):
    client = models.CharField(max_length=20)
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    desc = models.TextField()
    reserv_id = models.CharField(max_length=20, default="HaveToMod")
    status = models.IntegerField(default=1)
    status_bull = models.BooleanField(default=False)

    def __str__(self):
        return self.client + "_" + str(self.month) + str("/") + str(self.day) + " " + str(self.hour)+":"+str(self.minute)
