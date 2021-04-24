from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
import re
from .models import CustomUser, Location, Order
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.gis import forms as geoforms
"""

Create new forms for the custom user model

"""


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(label="Email", widget=forms.TextInput
                             (attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com',

                                     'id': 'email'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput
                                 (attrs={'class': 'form-control', 'placeholder': 'John', 'id': 'first_name', 'aria-describedby': 'validationServerfirst_name'}))

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


class CartForm(geoforms.Form):

    pin = geoforms.PointField(widget=geoforms.OSMWidget(
        attrs={'map_width': '100%', 'map_height': 'auto', 'default_lat': -1.2921, 'default_lon': 36.8219, 'default_zoom': 13}))
    # Must be filled if point is NULL || Blank
    floor = geoforms.CharField(label="Floor", widget=geoforms.TextInput
                               (attrs={'class': 'form-control', 'placeholder': 'Floor', 'id': 'floor'}))
    street = geoforms.CharField(label="Street", widget=geoforms.TextInput
                                (attrs={'class': 'form-control', 'placeholder': 'Street', 'id': 'street'}))
    apt = geoforms.CharField(label="Apartment", widget=geoforms.TextInput
                             (attrs={'class': 'form-control', 'placeholder': 'Apartment', 'id': 'apt'}))

    #geom = geoforms.PolygonField()


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.TextInput
                             (attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com',
                                     'id': 'email'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput
                                (attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'pass1'}))
    
class ProfileForm(geoforms.Form):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone')

class ProfileForm(UserChangeForm):
    email = forms.EmailField(label="Email", widget=forms.TextInput
                             (attrs={'class': 'form-control', 'placeholder': 'johndoe@example.com',

                                     'id': 'email'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput
                                 (attrs={'class': 'form-control', 'placeholder': 'John', 'id': 'first_name', 'aria-describedby': 'validationServerfirst_name'}))

    last_name = forms.CharField(label="Last Name", widget=forms.TextInput
                                (attrs={'class': 'form-control', 'placeholder': 'Doe', 'id': 'last_name'}))

    phone = forms.CharField(label="Phone Number", widget=forms.TextInput
                            (attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'id': 'phone'}))
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