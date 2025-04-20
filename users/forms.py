from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Film

class RegisterForm(UserCreationForm):
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ("username", "phone", "password1", "password2")

class LoginForm(AuthenticationForm):
    pass

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'