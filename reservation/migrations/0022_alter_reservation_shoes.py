# Generated by Django 4.2.9 on 2024-07-04 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0021_alter_reservation_shoes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="shoes",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reservation.shoes"
            ),
        ),
    ]
