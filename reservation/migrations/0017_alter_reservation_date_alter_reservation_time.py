# Generated by Django 4.2.9 on 2024-06-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reservation",
            "0016_alter_reservation_date_alter_reservation_reserv_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation", name="date", field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="reservation", name="time", field=models.TimeField(),
        ),
    ]
