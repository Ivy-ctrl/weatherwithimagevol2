import requests

def get_city_image(city_name):
    API_key = 'dh0kmGpsv6-gOPsY5J1m_sQGy3BDCrIUJZ7p4HHMesk'  # Replace with your actual Unsplash API key
    url = f'https://api.unsplash.com/search/photos?query={city_name}&client_id={API_key}&per_page=1'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:  # Check if we have results
            image_url = data['results'][0]['urls']['regular']  # Get the first image
            return image_url
        else:
            return None  # No image found
    else:
        return None  # Error occurred, no image
