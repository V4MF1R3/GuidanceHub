from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'skills', 'interests', 'bio')
    search_fields = ('user__username', 'role', 'skills', 'interests', 'bio')