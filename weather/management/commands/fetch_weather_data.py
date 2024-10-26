import requests
from django.core.management.base import BaseCommand
from django.utils import timezone
from weather.models import WeatherData

class Command(BaseCommand):
    help = 'Fetch weather data from OpenWeatherMap API'

    def handle(self, *args, **kwargs):
        api_key = 'f4ef13257d2adf1e8cd462538bba954e'
        cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
        url = "http://api.openweathermap.org/data/2.5/weather"

        for city in cities:
            params = {
                "q": city,
                "appid": api_key,
            }
            response = requests.get(url, params=params)
            data = response.json()

            if response.status_code == 200:
                WeatherData.objects.create(
                    city=city,
                    main=data['weather'][0]['main'],
                    temp=data['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
                    feels_like=data['main']['feels_like'] - 273.15,  # Convert from Kelvin to Celsius
                    dt=timezone.now()
                )
            else:
                self.stdout.write(self.style.ERROR(f"Failed to fetch data for {city}: {data.get('message', 'Unknown error')}"))
