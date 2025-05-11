from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_parking_admin')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_parking_admin')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('phone_number', 'address', 'is_parking_admin')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {'fields': ('phone_number', 'address', 'is_parking_admin')}),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')

admin.site.register(User, CustomUserAdmin)