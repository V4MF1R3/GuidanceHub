from django.contrib import admin
from .models import MentorshipRequest, MentorshipConnection

# Register your models here.
@admin.register(MentorshipRequest)
class MentorshipRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'status', 'timestamp')  # Fields to display in the list view
    list_filter = ('status', 'timestamp')  # Filters for the admin sidebar
    search_fields = ('sender__username', 'receiver__username')  # Searchable fields
    ordering = ('-timestamp',)  # Order by the most recent requests

@admin.register(MentorshipConnection)
class MentorshipConnectionAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'established_date')  # Fields to display in the list view
    search_fields = ('mentor__username', 'mentee__username')  # Searchable fields
    ordering = ('-established_date',)  # Order by the most recent connections