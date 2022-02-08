from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        labels = {
            'first_name': 'Nome',
            'last_name': 'Cognome',
        }
