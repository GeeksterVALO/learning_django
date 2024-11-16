from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('nickname', 'password')}),
        ('Personal info', {'fields': ('full_name', 'email', 'avatar', 'bio')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Favorites', {'fields': ('favorite_games',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nickname', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('nickname', 'email', 'full_name', 'is_staff')
    search_fields = ('nickname', 'email', 'full_name')
    ordering = ('nickname',)

admin.site.register(User, UserAdmin)
