# Generated by Django 3.2 on 2021-07-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='uploads/profile_pictures/default_profile_picture.jpeg', upload_to='uploads/profile_pictures'),
        ),
    ]