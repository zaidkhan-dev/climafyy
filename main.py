import os
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    city = request.args.get('city')
    
    if not city:
        return render_template('index.html', city_name=None)

    city_name = city.strip().lower().capitalize()
    
    api_key = "c80af8b2b8e24801ee72e884285feb96"
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

            return render_template(
                'index.html',
                city_name=city_name,
                temperature=temperature,
                feels_temp=feels_temp,
                humidity=humidity,
                wind_speed=wind_speed,
                wind_deg=wind_deg,
                description=description
            )
        else:
            return f"<h3>❌ Error: {data.get('message', 'Unable to fetch weather data')}</h3>"

    except Exception as e:
        return f"<h3>⚠️ An error occurred: {e}</h3>"
