from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


# ФОрма регитрации
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Форма измнения профайла
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


# Форма измнения профайла Изображения
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
