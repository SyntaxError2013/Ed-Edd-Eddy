from django.db import models

# Create your models here.

class Travel(models.Model):
    name = models.CharField(max_length=200)
    uri = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=75, null=True)
    
class Places(models.Model):
    """
    Markers on map
    """
    travel = models.ForeignKey(Travel)
    latti = models.FloatField()
    longi = models.FloatField()
    properties = models.TextField(null=True)
    location_name = models.CharField(max_length=200, null=True)
    date_time = models.DateTimeField(null=True)

class Activity(models.Model):
    """
    Comments on markers
    """
    place = models.ForeignKey(Places)
    comment = models.TextField(blank=False)
