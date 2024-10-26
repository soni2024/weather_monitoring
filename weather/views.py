from django.shortcuts import render
from weather.models import DailySummary, WeatherAlert

def index(request):
    summaries = DailySummary.objects.all()
    alerts = WeatherAlert.objects.all()
    return render(request, 'weather/index.html', {'summaries': summaries, 'alerts': alerts})
