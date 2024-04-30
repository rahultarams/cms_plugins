from django.contrib import admin
from .models import Properties
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')  # Columns to display in the admin list view
    search_fields = ('name', 'address')  # Fields to be searchable in the admin list view
    list_filter = ('address',)  # Filters on the right sidebar for quick filtering by address

admin.site.register(Properties, PropertyAdmin)