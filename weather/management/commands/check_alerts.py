# weather/management/commands/check_alerts.py

from django.core.management.base import BaseCommand
from weather.models import WeatherData, WeatherAlert
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings

class Command(BaseCommand):
    help = 'Check for weather alerts'

    def handle(self, *args, **kwargs):
        cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
        threshold_temp = 35.0

        for city in cities:
            recent_data = WeatherData.objects.filter(city=city).order_by('-dt')[:2]
            
            if recent_data.count() == 2 and all(data.temp > threshold_temp for data in recent_data):
                alert_message = f"Temperature exceeded {threshold_temp}°C for two consecutive updates in {city}"
                
                WeatherAlert.objects.create(
                    city=city,
                    condition=alert_message,
                    triggered_at=recent_data.first().dt
                )
                
                # Send email notification
                send_mail(
                    'Weather Alert',
                    alert_message,
                    settings.EMAIL_HOST_USER,
                    ['recipient@example.com'],  # Replace with actual recipient email
                    fail_silently=False,
                )
                
                self.stdout.write(self.style.SUCCESS(f"Alert triggered for {city}: {alert_message}"))

        self.stdout.write(self.style.SUCCESS("Finished checking alerts"))
