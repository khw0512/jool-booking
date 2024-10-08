# Generated by Django 4.2.9 on 2024-07-07 07:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0025_alter_bottom_link_alter_bottom_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("shoes", "Shoes"),
                            ("top", "Top"),
                            ("bottom", "Bottom"),
                            ("bag", "Bag & Pouch"),
                            ("etc", "ETC"),
                        ],
                        max_length=10,
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                (
                    "model_num",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            (
                                "shoes",
                                (
                                    ("220", "220mm"),
                                    ("225", "225mm"),
                                    ("230", "230mm"),
                                    ("235", "235mm"),
                                    ("240", "240mm"),
                                    ("245", "245mm"),
                                    ("250", "250mm"),
                                    ("255", "255mm"),
                                    ("260", "260mm"),
                                    ("265", "265mm"),
                                    ("270", "270mm"),
                                    ("275", "275mm"),
                                    ("280", "280mm"),
                                    ("285", "285mm"),
                                    ("290", "290mm"),
                                    ("295", "295mm"),
                                    ("300", "300mm"),
                                ),
                            ),
                            (
                                "top",
                                (
                                    ("XS", "XS"),
                                    ("S", "S"),
                                    ("M", "M"),
                                    ("L", "L"),
                                    ("XL", "XL"),
                                    ("XXL", "XXL"),
                                ),
                            ),
                            (
                                "bottom",
                                (
                                    ("XS", "XS"),
                                    ("S", "S"),
                                    ("M", "M"),
                                    ("L", "L"),
                                    ("XL", "XL"),
                                    ("XXL", "XXL"),
                                ),
                            ),
                        ],
                        max_length=10,
                    ),
                ),
                ("amount", models.IntegerField(default=0)),
                ("link", models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name="reservation",
            name="etc",
            field=models.ForeignKey(
                blank=True,
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="etcName",
                to="reservation.item",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="reservation",
            name="bottom",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bottomName",
                to="reservation.item",
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="shoes",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shoesName",
                to="reservation.item",
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="top",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="topName",
                to="reservation.item",
            ),
        ),
        migrations.DeleteModel(name="Bottom",),
        migrations.DeleteModel(name="Shoes",),
        migrations.DeleteModel(name="Top",),
    ]
