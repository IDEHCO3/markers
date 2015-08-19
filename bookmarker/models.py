from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bookmark(models.Model):

    LIST = (
        ('layer', 'Layer'),
        ('maps', 'Maps'),
        ('communities', 'Communities'),
        ('geoprojects', 'GeoProjects'),
    )

    url_origin = models.CharField(max_length=255)
    zoom = models.IntegerField(default=1)
    resourceType = models.CharField(choices=LIST, max_length=255, default='Communities')
    coordinates = models.CharField(max_length=1000, default='')
    user = models.ForeignKey(User)