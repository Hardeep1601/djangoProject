from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Form, UserModel


class NewUserForm(UserCreationForm):

    class Meta:
        model = UserModel
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

    # def save(self, commit=True):
    #     m = super(ClaimUser, self).save(commit=False)
    #     m.id = user

    def save(self, commit=True):
        user = super(ClaimUser, self).save(commit=False)
        id = self.cleaned_data["id"].split()
        user.id = id
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user