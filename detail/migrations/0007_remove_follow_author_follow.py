# Generated by Django 3.0.3 on 2023-01-09 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0006_auto_20230108_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='author_follow',
        ),
    ]
