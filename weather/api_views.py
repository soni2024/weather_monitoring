# weather/api_views.py
from rest_framework import viewsets
from .models import WeatherData, DailySummary
from .serializers import WeatherDataSerializer, DailySummarySerializer

class WeatherDataViewSet(viewsets.ModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class DailySummaryViewSet(viewsets.ModelViewSet):
    queryset = DailySummary.objects.all()
    serializer_class = DailySummarySerializer
