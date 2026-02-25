import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read API key securely from environment
api_key = os.getenv("API_KEY")

# Function to fetch weather data
def fetch_data(url):
    response = requests.get(url)
    data = response.json()

    # Check API response
    if data["cod"] != 200:
        return None, None, None

    city = data["name"]
    temperature = round(data["main"]["temp"] - 273.15, 1)  # Kelvin → Celsius
    description = data["weather"][0]["description"]

    return city, temperature, description


# Continuous loop for multiple searches
while True:
    user_input = input("Which city: ").strip().lower()

    if user_input == "exit":
        print("Exiting Weather App...")
        break

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"

    city, temperature, description = fetch_data(URL)

    if city:
        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Weather: {description}\n")
    else:
        print("ERROR! City not found\n")
