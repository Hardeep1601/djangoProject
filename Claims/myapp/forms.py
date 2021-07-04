from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Form, UserModel


class NewUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']


class ClaimUser(forms.ModelForm):
    # def __init__(self, user_id, *args, **kwargs):
    #     self.id = user_id
    #     super(ClaimUser, self).__init__(*args, **kwargs)

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
        if commit:
            user.save()
        return user
