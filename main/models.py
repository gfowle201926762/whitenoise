from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.utils import timezone
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Classroom(models.Model):
    students = models.ManyToManyField(User, related_name='student')
    teachers = models.ManyToManyField(User, related_name='teacher')
    title = models.CharField(max_length=50)
    LANGUAGE_CHOICES = (
        ('English','ENGLISH'),
        ('French', 'FRENCH'),
        ('Spanish','SPANISH'),
        ('Portuguese','PORTUGUESE'),
        ('German','GERMAN'),
        ('Danish','DANISH'),
        ('Dutch', 'DUTCH'),
        ('Russian','RUSSIAN'),
        ('Italian','ITALIAN'),
        ('Greek','GREEK'),
        ('Polish','POLISH'),
        ('Hindi','HINDI'),
        ('Finnish','FINNISH'),
        ('Hungarian','HUNGARIAN'),
        ('Czech','CZECH'),
        ('Welsh','WELSH'),
        ('Swedish','SWEDISH'),
    )
    native_language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    learning_language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)

class Post(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')


class Comment(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    name =models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='media/uploads/profile_pictures', default='media/uploads/profile_pictures/default_profile_picture.jpeg', blank=True)
    bio = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    following = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return f'{self.user.username} Profile'
        


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, name=instance.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    instance.profile.save()
