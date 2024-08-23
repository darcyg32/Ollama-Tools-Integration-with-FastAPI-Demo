import requests
import time

def get_current_weather(city:str) -> str:
    """
    Fetches the current weather for a specified city using the wttr.in API.

    Args:
        city (str): The name of the city to get the weather information for.

    Returns:
        str: A string containing the temperature in Celsius, or an error message if the request fails.
    """
    try:
        # Construct the URL for the API request, using the city name and JSON format
        base_url = f"http://wttr.in/{city}?format=j1"
        response = requests.get(base_url, timeout=5)  # Send a GET request to the API with a timeout of 5 seconds
        response.raise_for_status()  # Raise an exception if the response contains an HTTP error
        
        # Parse the JSON response to extract the temperature in Celsius
        data = response.json()
        temperature = data['current_condition'][0]['temp_C']
        # print(f"Weather in {city}: {temperature} degrees C")  # Debugging output
        return f"{temperature} degrees C"  # Return the temperature as a string
    except requests.RequestException as e:
        # Return an error message if the request fails due to network issues or server errors
        error_message = f"Error fetching weather data: {e}"
        # print(error_message)  # Debugging output
        return "Sorry, I'm unable to fetch the weather data right now due to service unavailability."
    except (KeyError, IndexError) as e:
        # Return an error message if the expected data format is not found in the API response
        error_message = f"Unexpected data format: {e}"
        # print(error_message)  # Debugging output
        return "Sorry, I couldn't find the weather information for that location."

def get_current_time() -> str:
    """
    Returns the current time formatted as HH:MM:SS.

    Returns:
        str: A string containing the current time in HH:MM:SS format.
    """
    return f"Time: {time.strftime('%H:%M:%S')}"

FUNCTION_REGISTRY = {
    'get_current_weather': get_current_weather,
    'get_current_time': get_current_time
}