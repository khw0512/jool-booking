# Generated by Django 5.0.6 on 2024-05-29 10:55

import reservation.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('client', models.CharField(max_length=20)),
                ('manager', models.CharField(max_length=30)),
                ('bag_img', models.ImageField(upload_to=reservation.models.image_upload_path)),
                ('desc', models.TextField()),
                ('finished', models.BooleanField(default=True)),
                ('month', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=20)),
                ('hour', models.CharField(max_length=20)),
                ('minute', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
