from django.core.serializers import serialize
from world.models import WorldBorder

serialize('geojson', WorldBorder.objects.all(),
          geometry_field='mpoly',
          fields=('fips', 'name'))

