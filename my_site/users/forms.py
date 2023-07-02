from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
          'username': forms.TextInput(attrs={'class': 'input is-medium'}),
          'email': forms.EmailInput(attrs={'class': 'input is-medium'}),
          'password1': forms.PasswordInput(attrs={'class': 'input is-medium'}),
          'password2': forms.PasswordInput(attrs={'class': 'input is-medium'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'date_of_birth', 'bio', 'instagram']


# class EditProfileForm(UserChangeForm):
#     email = forms.EmailField(widget=forms.EmailInput)
#     first_name = forms.CharField(max_length=40)
#     last_name = forms.CharField(max_length=40)
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']

