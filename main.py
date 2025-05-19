import os
import requests
import json
API_KEY = os.getenv("MY_API_KEY")
API_URL = os.getenv("MY_API_URL")
city_name =input("Enter a city name: ").strip().lower().upper().capitalize()

api_key = "c80af8b2b8e24801ee72e884285feb96"
api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(api_url)


try:
    data = response.json()

    # pretty_format = json.dumps(data, indent=4)
    # print(pretty_format)
    #to fetch specific data from json


    if response.status_code == 200:
        def about_weather(data):
            temperature = round(data["main"]["temp"])
            feels_temp = round(data["main"]["feels_like"])
            humidity = data["main"]["humidity"]
            print("WEATHER INFO:")
            print(f" 📈 Current temperature: {temperature}°C\n 👉 Feels like: {feels_temp}°C\n 💧 Humidity: {humidity}%")
        about_weather(data)
        print("\n WIND Info:")
        def wind(data):
            speed = data["wind"]["speed"]
            degree = data["wind"]["deg"]
            print(f"Speed: {speed} m/s \nDegree: {degree}")
        wind(data)
        def descr(data):
            description = data["weather"][0]["description"]
            print(f"Weather Description: {description}")
        descr(data)
    else:
        print(f"❌ Error: {data.get('message', 'Unable to fetch weather data')}")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")