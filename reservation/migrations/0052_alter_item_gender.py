# Generated by Django 4.2.9 on 2024-07-18 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0051_alter_item_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("M", "Male"), ("F", "Female"), ("E", "NO Gender")],
                max_length=1,
            ),
        ),
    ]
