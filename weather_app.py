import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read API key securely from environment
api_key = os.getenv("API_KEY")

# Function to fetch weather data from OpenWeather API
def fetch_data()
    # Send GET request to weather API
    response = requests.get(URL)
    # Convert API response to JSON format
    data = response.json()
    # Check if API request failed (city not found or error)
    if data["cod"] != 200:
        return None, None, None
    else:
        # Extract required weather details
        city = data["name"]
        temperature = round(data["main"]["temp"] - 273.15, 1)  # Kelvin → Celsius
        description = data["weather"][0]["description"]

        return city, temperature, description

# Continuous loop to allow multiple city searches
while True:
    # Take user input and normalize it
    user_input = input("Which city: ").strip().lower()
    # Exit condition
    if user_input == "exit":
        break
    # Build API URL dynamically using user input
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"
    # Fetch weather data
    city, temperature, description = fetch_data()
    # Display results
    if city:
        print(f"City: {city} Temperature: {temperature} Description: {description}")
    else:
        print("ERROR! City not found")
