from django import forms
from .models import Blog


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    confirm_password = forms.CharField()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']    