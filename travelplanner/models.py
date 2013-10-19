from django.db import models

# Create your models here.

class Travel(models.Model):
    name = models.CharField(max_length=200)
    uri = models.CharField(max_length=11, unique=True)
    
class Places(models.Model):
    """
    Markers on map
    """
    travel = models.ForeignKey(Travel)
    latti = models.FloatField()
    longi = models.FloatField()
    properties = models.TextField()
    location_name = models.CharField(max_length=200)
    date_time = models.DateTimeField()

class Activity(models.Model):
    """
    Comments on markers
    """
    map_point = models.ForeignKey(Map)
    comment = models.TextField()
