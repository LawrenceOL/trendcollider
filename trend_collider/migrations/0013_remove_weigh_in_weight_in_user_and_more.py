# Generated by Django 4.0.4 on 2022-05-15 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trend_collider', '0012_auto_20220512_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weigh_in',
            name='weight_in_user',
        ),
        migrations.AddField(
            model_name='weigh_in',
            name='weigh_in_user',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
