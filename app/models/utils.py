import requests
from dotenv import load_dotenv
import os

load_dotenv()

weather_api_key = os.getenv("WEATHER_API_KEY")

def fetch_weather(city : str) -> dict:

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key' : weather_api_key,
        'q' : city
    }
    response = requests.get(url=url, params=params)
    return response.json()