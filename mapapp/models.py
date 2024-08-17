from django.db import models

class PointData(models.Model):
    name = models.CharField(max_length=100)
    location = models.JSONField()

class PolygonData(models.Model):
    name = models.CharField(max_length=100)
    area = models.JSONField()
