from django.contrib.gis.db import models

# Create your models here.
class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()
    #Geodjango specific: a geometry field (multi polygon)
    mpoly = models.MultiPolygonField()
    #returns the string representation of the model
    def __str__(self):
        return self.name

#healthFacilities model
class healthFacilities(models.Model):
    f_name = models.CharField(max_length=50, null=True)
    prov = models.CharField(max_length=50, null=True)
    dist = models.CharField(max_length=50, null=True)
    division = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    sub_locati = models.CharField(max_length=50, null=True)
    long = models.FloatField(null=False)
    lat = models.FloatField(null=False)
    spatial_re = models.CharField(max_length=50, null=True)
    f_type = models.IntegerField(null=True)
    agency = models.CharField(max_length=50, null=True)
    # Geodjango specific: a geometry field (multipoint)
    geom = models.PointField(srid=4326)

    #returns the string representation of the model
    def __str__(self):
        return self.f_name

    @property
    def popupContent(self):
        return {'f_name': self.f_name, 'f_type': self.f_type, 'prov':self.prov,'geom':self.geom}





