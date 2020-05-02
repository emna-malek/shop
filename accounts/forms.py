from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import userProfile
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    template_name = '/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',

        )


class UserProfile(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = [
            'phone',
            'city',
            'company',
            'image',
        ]


User = get_user_model()
