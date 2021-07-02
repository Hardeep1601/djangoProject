from django.contrib import admin

# Register your models here.

from .models import Form

class formClaims(admin.ModelAdmin):
    list_display = (
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
    )


admin.site.register(Form, formClaims)
