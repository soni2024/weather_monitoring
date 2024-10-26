# weather/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import WeatherDataViewSet, DailySummaryViewSet
from . import views

router = DefaultRouter()
router.register(r'weatherdata', WeatherDataViewSet)
router.register(r'dailysummaries', DailySummaryViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
]


