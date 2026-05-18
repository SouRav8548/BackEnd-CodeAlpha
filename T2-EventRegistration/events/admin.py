from django.contrib import admin
from .models import Event, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # What columns to show in the list view
    list_display = ('title', 'date', 'location', 'capacity', 'created_at', 'registration_count')
    
    # Add filter options on the right side
    list_filter = ('date', 'location')
    
    # Add search box
    search_fields = ('title', 'description', 'location')
    
    # Default ordering
    ordering = ('date',)
    
    # Organize fields when adding/editing
    fieldsets = (
        ('Event Information', {
            'fields': ('title', 'description')
        }),
        ('Date & Location', {
            'fields': ('date', 'location')
        }),
        ('Capacity', {
            'fields': ('capacity',)
        }),
    )
    
    def registration_count(self, obj):
        """Show number of registrations for each event"""
        return obj.registrations.count()
    registration_count.short_description = 'Registrations'

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('participant', 'event', 'registered_at')
    list_filter = ('event', 'registered_at')
    search_fields = ('participant__username', 'event__title')
    ordering = ('-registered_at',)
    raw_id_fields = ('participant',)  # Better for when you have many users