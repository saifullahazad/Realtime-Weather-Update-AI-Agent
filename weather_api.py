# weather_api.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_live_weather(location: str) -> dict:
    """
    Call the live weather API to get current weather data for a given location.
    Returns a dictionary with weather data.
    """
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    print("\n\n Weather API URL : " + url+" \n\n")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Example: {'location': {...}, 'current': {...}}
    else:
        return {"error": f"Failed to fetch weather data. Status Code: {response.status_code}"}
