# Generated by Django 4.2.9 on 2024-06-24 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0011_alter_reservation_date_alter_reservation_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation", name="date", field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="reservation", name="time", field=models.TimeField(null=True),
        ),
    ]
