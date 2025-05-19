import os
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    city = request.args.get('city')
    if not city:
        return '''
            <h2>Enter a City Name</h2>
            <form method="get">
                <input type="text" name="city" required />
                <input type="submit" value="Get Weather" />
            </form>
        '''

    city_name = city.strip().lower().capitalize()
    api_key = "c80af8b2b8e24801ee72e884285feb96"  # replace with os.getenv("MY_API_KEY") in production
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(api_url)
        data = response.json()

        if response.status_code == 200:
            temperature = round(data["main"]["temp"])
            feels_temp = round(data["main"]["feels_like"])
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            wind_deg = data["wind"]["deg"]
            description = data["weather"][0]["description"]

            return f"""
                <h3>Weather for {city_name}:</h3>
                <ul>
                    <li>🌡️ Temperature: {temperature}°C</li>
                    <li>🤔 Feels Like: {feels_temp}°C</li>
                    <li>💧 Humidity: {humidity}%</li>
                    <li>🌬️ Wind Speed: {wind_speed} m/s</li>
                    <li>🧭 Wind Direction: {wind_deg}°</li>
                    <li>📖 Description: {description}</li>
                </ul>
                <a href="/">Search another city</a>
            """
        else:
            return f"<h3>❌ Error: {data.get('message', 'Unable to fetch weather data')}</h3>"

    except Exception as e:
        return f"<h3>⚠️ An error occurred: {e}</h3>"
