import streamlit as st
import requests

API_KEY = "YOUR API KEY"  # Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        return None

st.title("Weather App 🌤")
city = st.text_input("Enter city name:", "Mumbai")

if st.button("Get Weather"):
    weather_data = get_weather(city)
    if weather_data:
        st.subheader(f"Weather in {weather_data['city']}")
        st.write(f"🌡 Temperature: {weather_data['temperature']}°C")
        st.write(f"🌦 Condition: {weather_data['weather']}")
        st.write(f"💧 Humidity: {weather_data['humidity']}%")
        st.write(f"🌬 Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        st.error("City not found! Please enter a valid city name.")
