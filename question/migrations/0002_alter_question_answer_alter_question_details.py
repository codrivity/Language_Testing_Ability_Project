# Generated by Django 4.2.3 on 2023-08-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("question", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question", name="answer", field=models.CharField(),
        ),
        migrations.AlterField(
            model_name="question", name="details", field=models.CharField(),
        ),
    ]
