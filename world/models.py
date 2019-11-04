from django.db import models
from django.contrib.gis.db import models
# Create your models here.
class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    location = models.PointField(default='Story')
    address = models.CharField(max_length=100, default='Heya')
    city = models.CharField(max_length=50, default='Howye')

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name