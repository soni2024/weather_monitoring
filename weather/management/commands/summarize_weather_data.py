# weather/management/commands/summarize_weather_data.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import Avg, Max, Min, Count
from weather.models import WeatherData, DailySummary

class Command(BaseCommand):
    help = 'Summarize daily weather data'

    def handle(self, *args, **kwargs):
        cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
        today = timezone.now().date()

        for city in cities:
            weather_data = WeatherData.objects.filter(city=city, dt__date=today)
            if weather_data.exists():
                daily_summary = weather_data.aggregate(
                    average_temp=Avg('temp'),
                    max_temp=Max('temp'),
                    min_temp=Min('temp'),
                    dominant_condition=Count('main')  # This needs more logic for actual dominant condition
                )

                DailySummary.objects.create(
                    city=city,
                    date=today,
                    average_temp=daily_summary['average_temp'],
                    max_temp=daily_summary['max_temp'],
                    min_temp=daily_summary['min_temp'],
                    dominant_condition=weather_data.values('main').annotate(count=Count('main')).order_by('-count').first()['main']  # Find dominant condition
                )
