# Generated by Django 3.2 on 2021-07-05 16:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0015_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
    ]
