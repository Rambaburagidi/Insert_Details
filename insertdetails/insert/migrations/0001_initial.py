# Generated by Django 4.2.3 on 2023-09-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="insert",
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
                ("empid", models.IntegerField()),
                ("empname", models.CharField(max_length=100)),
                ("deg", models.CharField(max_length=100)),
                ("salary", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("place", models.CharField(max_length=100)),
                ("phone", models.BigIntegerField()),
                ("photo", models.ImageField(upload_to="image/")),
            ],
        ),
    ]
