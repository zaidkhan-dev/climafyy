from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

API_KEY = "c80af8b2b8e24801ee72e884285feb96"

@app.route('/weather', methods=['GET'])
def get_weather():
    city_name = request.args.get('city')
    if not city_name:
        return jsonify({'error': 'City not provided'}), 400

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:
        result = {
            "temperature": round(data["main"]["temp"]),
            "feels_like": round(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"]["deg"],
            "description": data["weather"][0]["description"]
        }
        return jsonify(result)
    else:
        return jsonify({"error": data.get("message", "Unable to fetch weather data")}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
