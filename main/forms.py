from django import forms
from django.forms.widgets import DateInput
from .models import Post, Comment, UserProfile, Classroom

class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Make a post...'
        })
    )
    class Meta:
        model = Post
        fields = ['body']


class CommentForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows': 1,
            'placeholder': 'Make a comment...'
        })
    )
    class Meta:
        model = Comment
        fields = ['body']


class UserProfileForm(forms.ModelForm):
    image = forms.ImageField(
        label='Profile Picture',
        widget=forms.FileInput
    )
    bio = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'rows' : 3,
        'placeholder' : 'What describes you best?'
    }))
    class Meta:
        model = UserProfile
        fields = ['name', 'image', 'birthday', 'bio']
        widgets = {
            'birthday': DateInput(),
        }



class ClassroomForm(forms.ModelForm):
    
    class Meta:
        model = Classroom
        fields = ['title', 'teachers', 'students', 'native_language', 'learning_language']