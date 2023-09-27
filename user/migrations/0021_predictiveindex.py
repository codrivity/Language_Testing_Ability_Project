# Generated by Django 4.2.4 on 2023-09-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0020_delete_predictiveindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="PredictiveIndex",
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
                ("language", models.CharField(max_length=100)),
                ("fname", models.TextField(max_length=100)),
                ("mname", models.TextField(max_length=100)),
                ("lname", models.TextField(default=None, max_length=100)),
                ("email", models.TextField(max_length=100)),
                ("pi_id", models.TextField(max_length=100)),
                ("age", models.TextField(max_length=100)),
                ("gender", models.TextField(max_length=100)),
                ("race", models.TextField(max_length=100)),
                ("education", models.TextField(max_length=100)),
            ],
        ),
    ]