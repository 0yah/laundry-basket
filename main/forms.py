from django.contrib.auth.forms import UserChangeForm, UserCreationForm
import re
from .models import CustomUser
from django import forms
from django.core.exceptions import ValidationError

"""

Create new forms for the custom user model

"""


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(label="Email", widget=forms.TextInput
                             (attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com',

                                     'id': 'email'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput
                                 (attrs={'class': 'form-control', 'placeholder': 'John', 'id': 'first_name','aria-describedby':'validationServerfirst_name'}))

    last_name = forms.CharField(label="Last Name", widget=forms.TextInput
                                (attrs={'class': 'form-control', 'placeholder': 'Doe', 'id': 'last_name'}))

    phone = forms.CharField(label="Phone Number", widget=forms.TextInput
                            (attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'id': 'phone'}))

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput
                                (attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'pass1'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput
                                (attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'id': 'pass2'}))

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Test for the Kenyan Country Code
        result = re.match(
            '^[+]*2547[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', phone)
        if result is None:
            raise ValidationError("You entered an invalid Phone Number!")

        return phone

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone')


class CustomUserChangeForm(UserChangeForm):
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Test for the Kenyan Country Code
        result = re.match(
            '^[+]*2547[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$', phone)
        if result is None:
            raise ValidationError("You entered an invalid Phone Number!")

        return phone

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone')
