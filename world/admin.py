from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import WorldBorder
# Register your models here.
@admin.register(WorldBorder)
class WorldAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')