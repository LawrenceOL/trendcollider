# Generated by Django 4.0.4 on 2022-05-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend_collider', '0004_auto_20220512_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_pick',
            name='symbol',
            field=models.CharField(max_length=15),
        ),
    ]
