from django.urls import path
from django.conf.urls import include
# Views
from .views import WeatherView

urlpatterns = [
    path('weather/', WeatherView.as_view()),
]