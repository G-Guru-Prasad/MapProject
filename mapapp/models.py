from django.db import models

class PointData(models.Model):
    name = models.CharField(max_length=100)
    location = models.JSONField()  # Store point data as JSON

class PolygonData(models.Model):
    name = models.CharField(max_length=100)
    area = models.JSONField()  # Store polygon data as JSON
