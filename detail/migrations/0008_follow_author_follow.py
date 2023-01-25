# Generated by Django 3.0.3 on 2023-01-09 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('detail', '0007_remove_follow_author_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='author_follow',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
