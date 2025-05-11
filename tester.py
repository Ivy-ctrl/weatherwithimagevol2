import requests

def get_weather_and_image(city_name):
    API_key = '38a6fdafd7ead5f43eb6fc8ac4707352'
    url_weather =f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

    API_key_unsplash = 'dh0kmGpsv6-gOPsY5J1m_sQGy3BDCrIUJZ7p4HHMesk'
    url_unsplash = f'https://api.unsplash.com/search/photos?query={city_name}&client_id={API_key_unsplash}&per_page=1'

    response_weather = requests.get(url_weather)
    weather_data = None
    if response_weather.status_code == 200:
        data_weather = response_weather.json()
        weather_data = {
            'description': data_weather['weather'][0]['description'],
            'temperature': data_weather['main']['temp']
        }
    response_unsplash = requests.get(url_unsplash)
    image_url = None
    if response_unsplash.status_code == 200:
        data_unsplash = response_unsplash.json()
        if data_unsplash['results']:
            image_url = data_unsplash['results'][0]['urls']['regular']

    return weather_data, image_url