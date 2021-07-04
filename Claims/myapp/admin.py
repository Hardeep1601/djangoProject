from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import Form, UserModel


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


class UserInfo(UserAdmin):
    fieldsets = UserAdmin.fieldsets




admin.site.register(Form, formClaims)
# admin.site.unregister(UserModel)
admin.site.register(UserModel, UserInfo)
