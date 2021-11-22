from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Chatroom(models.Model):
    title = models.CharField(max_length=50)
    members = models.ManyToManyField(User, related_name='chatrooms')

    def __str__(self):
        return self.title

    