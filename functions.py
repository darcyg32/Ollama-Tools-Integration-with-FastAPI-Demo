import requests
import time

def get_current_weather(city:str) -> str:
    """Get the current weather for a city
    Args:
        city: The city to get the weather for
    """
    try:
        base_url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        temperature = data['current_condition'][0]['temp_C']
        return f"The current temperature in {city} is: {temperature}°C"
    except requests.RequestException as e:
        return f"Error fetching weather data: {e}"
    except (KeyError, IndexError) as e:
        return f"Unexpected data format: {e}"

def get_current_time() -> str:
    """Get the current time"""
    current_time = time.strftime("%H:%M:%S")
    return f"The current time is {time.strftime('%H:%M:%S')}"

FUNCTION_REGISTRY = {
    'get_current_weather': get_current_weather,
    'get_time': get_current_time
}