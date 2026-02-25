import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
def fetch_data():
        response = requests.get(URL)
        data = response.json()
        if data["cod"] != 200:
            return None, None, None
        else:
            city = data["name"]
            temparature = round(data["main"]["temp"] - 273.15, 1)
            description = data["weather"][0]["description"]
            return city, temparature, description
while True:
    user_input = input("Which city: ").strip().lower()
    if user_input == "exit":
        break
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"
    

    city, temparature, description = fetch_data()
    if city:
        print(f"city: ", city, "Temparature: ", temparature, "Description: ", description)
    else:
        print("ERROR! City not found")
    
    







    
