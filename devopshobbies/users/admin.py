from django.contrib import admin
from .models import BaseUser
# Register your models here.

@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('ID',
        'first_name',
        'last_name',
        'email',
        'is_admin',
        'is_active',
        'is_superuser',
        'created_at',
        )