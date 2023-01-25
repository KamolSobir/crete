from django import forms
from .models import Login, Post
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, PhotoCreate

User = get_user_model()


class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }


class Photoform(forms.ModelForm):
    class Meta:
        model = PhotoCreate
        fields = '__all__'
        # ('author', 'photos', 'data_photo')


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class LoginForm(forms.ModelForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': forms}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': forms}))

    class Meta:
        model = Login
        fields = ('username', 'password')
