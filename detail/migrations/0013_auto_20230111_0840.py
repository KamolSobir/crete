# Generated by Django 3.0.3 on 2023-01-11 03:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detail', '0012_auto_20230110_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='follow',
        ),
        migrations.AddField(
            model_name='photocreate',
            name='follow',
            field=models.ManyToManyField(null=True, related_name='create', to=settings.AUTH_USER_MODEL),
        ),
    ]
