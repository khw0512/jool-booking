# Generated by Django 4.2.9 on 2024-06-24 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0009_reservation_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="time",
            field=models.TimeField(auto_now_add=True),
        ),
    ]
