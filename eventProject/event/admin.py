from django.contrib import admin
from .models import Category, Event, EventTag, EventImages, Country, State, City

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'isActive', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']

@admin.register(EventTag)
class EventTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'isActive', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'country', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug', 'country__name']
    list_filter = ['country']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'state', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug', 'state__name']
    list_filter = ['state__country', 'state']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'country', 'state', 'city', 'event_date', 'created_at', 'updated_at']
    readonly_fields = ['slug', 'created_at', 'updated_at']
    search_fields = ['title', 'slug', 'venue']
    list_filter = ['is_active', 'category', 'country', 'state', 'city', 'event_date']

admin.site.register(EventImages)