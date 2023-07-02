from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from .models import Profile


class UserRegisterForm(UserCreationForm):



    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs):
    #     self.fields['username'] .widget.attrs['class'] = 'Username'
    #     self.fields['email']    .widget.attrs['class'] = 'Email'
    #     self.fields['password1'].widget.attrs['class'] = 'Password'
    #     self.fields['password2'].widget.attrs['class'] = 'Confirm Password'






class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'date_of_birth', 'bio', 'instagram']





class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'input is-medium',
                'placeholder': 'example@email.com',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'input is-medium',
                'placeholder': '************',
            }
        )
    )




# class EditProfileForm(UserChangeForm):
#     email = forms.EmailField(widget=forms.EmailInput)
#     first_name = forms.CharField(max_length=40)
#     last_name = forms.CharField(max_length=40)
#
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']

