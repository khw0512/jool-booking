# Generated by Django 4.2.9 on 2024-07-04 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0019_reservation_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shoes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=50)),
                ("amount250", models.IntegerField()),
                ("amount260", models.IntegerField()),
                ("amount270", models.IntegerField()),
                ("amount280", models.IntegerField()),
                ("link", models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name="reservation",
            name="bottom",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="reservation", name="desc", field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="top",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="shoes",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reservation.shoes"
            ),
        ),
    ]
