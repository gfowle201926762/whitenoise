from django.contrib import admin

from .models import Comment, Post, UserProfile, Classroom

myModels = [Comment, Post, UserProfile, Classroom]

admin.site.register(myModels)