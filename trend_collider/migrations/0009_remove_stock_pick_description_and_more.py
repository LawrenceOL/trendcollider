# Generated by Django 4.0.4 on 2022-05-12 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trend_collider', '0008_auto_20220512_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock_pick',
            name='description',
        ),
        migrations.AlterField(
            model_name='stock_pick',
            name='symbol',
            field=models.CharField(max_length=5),
        ),
    ]