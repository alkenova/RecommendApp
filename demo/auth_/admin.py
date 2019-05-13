from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from .models import MainUser
from django.utils.translation import gettext as _


@admin.register(MainUser)
class MyMainUser(UserAdmin):
    list_display = ('username', 'email', 'full_name',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',),
        }),
    )
    list_filter = ('is_superuser', 'is_active',)
    search_fields = ('username', 'full_name', 'email')

