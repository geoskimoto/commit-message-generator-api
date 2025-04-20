import requests

def get_weather(city):
    try:
        response = requests.get(f"http://api.weather.com/{city}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
