# weather/models.py
from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    temp = models.FloatField()
    feels_like = models.FloatField()
    dt = models.DateTimeField()

class DailySummary(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    average_temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    dominant_condition = models.CharField(max_length=100)


class WeatherAlert(models.Model):
    city = models.CharField(max_length=100)
    condition = models.CharField(max_length=255)
    triggered_at = models.DateTimeField()
