from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Icon_Weather
from scripts.find_location import get_city, get_location
import requests
from fiscal_code.settings import weather_key

# Create your views here.
class WeatherView(APIView):
    def get(self, request):
        # Set the variable "url" to have the value
        city = get_city()
        key = weather_key
        url = 'http://api.weatherapi.com/v1/current.json?key=' + key + '&q=' + city + '&aqi=no'

        # Make the request
        response = requests.get(url)

        # Get the JSON from the response
        weather_json = response.json()
        # Get the JSON from the response
        # print(weather_json)

        # Check if there was an error print error message
        if weather_json.get('error') is not None:
            print('Error:', weather_json.get('error').get('message'))
            exit(1)
        else:
            # Get the weather data
            location = weather_json.get('location').get('name')

            temp = weather_json.get('current').get('temp_c')

            description = weather_json.get('current').get('condition').get('text')

            code = weather_json.get('current').get('condition').get('code')

            # Get transcoding code img for weather icons
            image = Icon_Weather.objects.get(image_code=code)
            imageWeather = image.image_url
            # Print the data
            '''
            print('Weather in', location)
            print('The temperature is', temp, 'degrees Celsius')
            print('The description is', description)
            print('Location', get_location())
            '''
        # Return the data
        return Response({'location': location, 'temp': temp, 'description': description, 'code': code, 'imageWeather': imageWeather})