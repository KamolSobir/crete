# Generated by Django 3.0.3 on 2023-01-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0013_auto_20230111_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photocreate',
            name='photos',
            field=models.ImageField(upload_to='media/image/png-my-account-icon-blue.png', verbose_name='Изображение'),
        ),
    ]
