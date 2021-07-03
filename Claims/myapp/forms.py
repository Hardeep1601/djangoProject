from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Form


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ClaimUser(forms.ModelForm):
    class Meta:
        model = Form
        fields = [
            'name',
            'email',
            'contact_num',
            'vehicle_year_make',
            'vehicle_model',
            'vehicle_num',
            'date',
            'time',
            'location',
            'description',
            'report',
            'injury',
            'photo',
            'document'
        ]
