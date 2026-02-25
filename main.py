import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("API_KEY")

# ---------------- UI ----------------
st.title("🌦 Live Weather App")

city_input = st.text_input("Enter City Name")

# -------- Weather Fetch Function -----
def fetch_data(city):
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(URL)
    data = response.json()

    if data["cod"] != 200:
        return None, None, None

    city_name = data["name"]
    temperature = round(data["main"]["temp"] - 273.15, 1)
    description = data["weather"][0]["description"]

    return city_name, temperature, description


# -------- Logic Trigger --------------
if city_input:
    city_input = city_input.strip().lower()

    city, temperature, description = fetch_data(city_input)

    if city:
        st.success(f"City: {city}")
        st.write(f"🌡 Temperature: {temperature}°C")
        st.write(f"☁️ Weather: {description}")
    else:
        st.error("City not found")
    
    







    
