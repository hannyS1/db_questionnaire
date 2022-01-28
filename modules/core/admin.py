from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin as UserAdminContrib

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(User)
class UserAdmin(UserAdminContrib):
    list_display = ['username']

    fieldsets = (
        [None, {
            'fields': ['username', 'password', 'is_staff', 'is_superuser']
        }],
    )
