from django.contrib import admin

# Register your models here.

from .models import Form, UserAccount


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


class UserInfo(admin.ModelAdmin):
    list_display = (
        'name',
        'email'
    )

admin.site.register(Form, formClaims)
admin.site.register(UserAccount, UserInfo)
