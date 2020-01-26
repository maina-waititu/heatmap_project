from django.contrib.gis import admin
from .models import WorldBorder, healthFacilities

from leaflet.admin import LeafletGeoAdmin

# class WorldAdmin(LeafletGeoAdmin):
#      #fields to show in admin list view
#      list_display = ('name', 'Mpoly')



# Register your models here.
admin.site.register(WorldBorder, LeafletGeoAdmin)
# admin.site.register(healthFacilities, admin.GeoModelAdmin)

@admin.register(healthFacilities)
class healthAdmin(LeafletGeoAdmin):
    list_display = ('f_name','prov','f_type','location')