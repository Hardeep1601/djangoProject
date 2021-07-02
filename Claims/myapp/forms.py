
from django import forms
from .models import Form


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

