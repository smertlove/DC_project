from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):


    # email = forms.EmailField()

    # birth_year = forms.DateField(
    #     widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    # )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
          'username': forms.TextInput(attrs={'class': 'input is-medium'}),
          'email': forms.EmailInput(attrs={'class': 'input is-medium'}),
          'password1': forms.PasswordInput(attrs={'class': 'input is-medium'}),
          'password2': forms.PasswordInput(attrs={'class': 'input is-medium'}),
        }