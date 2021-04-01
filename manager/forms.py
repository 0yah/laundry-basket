from django.contrib.auth.forms import UserChangeForm, UserCreationForm
import re
from main.models import CustomUser, Location, Order,Item
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.gis import forms as geoforms

class ItemForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput
                                 (attrs={'class': 'form-control', 'placeholder': 'Item Name', 'id': 'name', 'aria-describedby': 'validationServerfirst_name'}))

    price = forms.CharField(label="Price", widget=forms.TextInput
                                (attrs={'class': 'form-control', 'placeholder': 'Item Price', 'id': 'name'}))
    class Meta:
        model = Item
        fields = ("name","price")
