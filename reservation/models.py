from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from ckeditor_uploader.fields import RichTextUploadingField

def image_upload_path(instance, filename):
    time=timezone.now()
    return f'{instance}/{titme}+{filename}'

class Item(models.Model):

    CATEGORY = [
        ('shoes','Shoes'),
        ('top','Top'),
        ('bottom','Bottom'),
        ('bag','Bag & Pouch'),
        ('etc','ETC')
    ]

    SIZE = [
        ('Others','free'),
        ('shoes',(
            ('220','220mm'),
            ('225','225mm'),
            ('230','230mm'),
            ('235','235mm'),
            ('240','240mm'),
            ('245','245mm'),
            ('250','250mm'),
            ('255','255mm'),
            ('260','260mm'),
            ('265','265mm'),
            ('270','270mm'),
            ('275','275mm'),
            ('280','280mm'),
            ('285','285mm'),
            ('290','290mm'),
            ('295','295mm'),
            ('300','300mm'),
        )),
        ('top',(
            ('XS','XS'),
            ('S','S'),
            ('M','M'),
            ('L','L'),
            ('XL','XL'),
            ('XXL','XXL'),
        )),
        ('bottom',(
            ('XS','XS'),
            ('S','S'),
            ('M','M'),
            ('L','L'),
            ('XL','XL'),
            ('XXL','XXL'),
        ))
    ]

    GENDER = {
        ('M','Male'),
        ('F','Female'),
        ('E','NO Gender')
    }
    

    category = models.CharField(max_length=10, choices=CATEGORY)
    gender = models.CharField(max_length=1, blank=True, choices=GENDER)
    name = models.CharField(max_length=20, blank=True)
    model_num = models.CharField(primary_key=True, max_length=50, blank=True)
    size = models.CharField(max_length=10, blank=True, choices=SIZE)
    amount = models.IntegerField(default=0, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.model_num

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
    contact = models.CharField(max_length=50, blank=False)
    start_date = models.DateField()
    start_time = models.TimeField(blank=True, default=timezone.now)
    end_date = models.DateField()
    end_time = models.TimeField(blank=True, default=timezone.now)
    top = models.ForeignKey(Item, on_delete=models.CASCADE, limit_choices_to={'category':'top'}, related_name="topName", blank=True, null=True)
    bottom = models.ForeignKey(Item, on_delete=models.CASCADE, limit_choices_to={'category':'bottom'}, related_name="bottomName", blank=True, null=True)
    shoes = models.ForeignKey(Item, on_delete=models.CASCADE, limit_choices_to={'category':'shoes'}, related_name="shoesName", blank=True, null=True)
    bag = models.ForeignKey(Item, on_delete=models.CASCADE, limit_choices_to={'category':'bag'}, related_name="bagName", blank=True, null=True)
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

