# Generated by Django 4.0.4 on 2022-05-11 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trend_collider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_pick',
            name='created',
        ),
        migrations.RemoveField(
            model_name='stock_pick',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='weigh_in',
            name='created',
        ),
        migrations.RemoveField(
            model_name='weigh_in',
            name='modified',
        ),
    ]
