import requests
import json

url = 'https://api.ipify.org'

def get_city():
    ip_address = requests.get(url).text
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')

    if response.status_code == 200:
        data = json.loads(response.text)
        city = data['city']
        return city
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None


def get_location():
    ip_address = requests.get(url).text
    response = requests.get(f'https://ipinfo.io/{ip_address}/json')

    # Check for successful request before processing
    if response.status_code == 200:
        data = json.loads(response.text)
        city = data['city']
        region = data['region']
        country = data['country']
        loc = data['loc']
        org = data['org']
        '''
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Location: {loc}")
        print(f"Org: {org}")
        '''
        # Return the entire response object for further processing (optional)
        return response
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None  # Or handle the error differently
