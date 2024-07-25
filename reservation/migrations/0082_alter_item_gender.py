# Generated by Django 4.2.9 on 2024-07-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0081_alter_item_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("E", "NO Gender"), ("F", "Female")],
                max_length=1,
            ),
        ),
    ]
