import requests

# Set the variable "url" to have the value
city = input('Enter the name of a city: ')
key = 'b7c4a813f27143f4bdb123103240409'
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

    # Print the data
    print('Weather in', location)
    print('The temperature is', temp, 'degrees Celsius')
    print('The description is', description)
    print('The code is', code)
