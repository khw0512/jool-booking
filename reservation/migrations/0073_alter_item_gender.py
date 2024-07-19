# Generated by Django 4.2.9 on 2024-07-19 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0072_alter_item_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("E", "NO Gender"), ("M", "Male"), ("F", "Female")],
                max_length=1,
            ),
        ),
    ]
