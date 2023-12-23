from django.contrib import admin

from authapp.models import CustomUser

# Register your models here.
class CustomUserDisplay(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'username', 'user_type']
admin.site.register(CustomUser, CustomUserDisplay)