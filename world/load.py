import os
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder, healthFacilities


world_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'mpoly': 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'TM_WORLD_BORDERS-0.3.shp'),)

def run_1(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


#healthFacilities
# Auto-generated `LayerMapping` dictionary for healthFacilities model
healthfacilities_mapping = {
    'f_name': 'F_NAME',
    'prov': 'PROV',
    'dist': 'DIST',
    'division': 'DIVISION',
    'location': 'LOCATION',
    'sub_locati': 'SUB_LOCATI',
    'long': 'LONG',
    'lat': 'LAT',
    'spatial_re': 'SPATIAL_RE',
    'f_type': 'F_TYPE',
    'agency': 'AGENCY',
    'geom': 'POINT',
}



health_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'healthFacilities3.geojson'),)

def run(verbose=True):
    lm_h = LayerMapping(healthFacilities, health_shp, healthfacilities_mapping, transform=False)
    lm_h.save(strict=True, verbose=verbose)