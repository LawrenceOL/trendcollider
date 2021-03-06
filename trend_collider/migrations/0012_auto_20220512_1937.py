# Generated by Django 4.0.4 on 2022-05-12 19:37

from django.db import migrations
from django.conf import settings


def create_data(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User(pk=2, email="satchl16@gmail.com",
                date_of_birth="1989-09-29")
    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('trend_collider', '0011_stock_pick_description'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
