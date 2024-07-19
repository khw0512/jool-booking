# Generated by Django 4.2.9 on 2024-07-19 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0075_alter_item_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("F", "Female"), ("E", "NO Gender"), ("M", "Male")],
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="paypal_link",
            field=models.TextField(blank=True, default="free"),
        ),
    ]
