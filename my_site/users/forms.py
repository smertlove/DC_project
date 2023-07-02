from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "example@email.com",
                "class": "input is-medium"
            }
        )
    )

    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "example@email.com",
                "class": "input is-medium"
            }
        )
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "************",
                "class": "input is-medium"
            }
        )
    )


    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "************",
                "class": "input is-medium"
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']



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

