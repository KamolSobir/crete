# Generated by Django 3.0.3 on 2023-01-07 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photocreate',
            old_name='author_photo',
            new_name='photo',
        ),
    ]
