from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

# Simulated weather data for different cities
WEATHER_DATA = {
    'New York': {'temp_range': (20, 85), 'conditions': ['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy']},
    'London': {'temp_range': (40, 70), 'conditions': ['Cloudy', 'Rainy', 'Foggy', 'Partly Cloudy']},
    'Tokyo': {'temp_range': (35, 90), 'conditions': ['Sunny', 'Cloudy', 'Rainy', 'Humid']},
    'Paris': {'temp_range': (35, 80), 'conditions': ['Sunny', 'Cloudy', 'Rainy', 'Windy']},
    'Sydney': {'temp_range': (50, 95), 'conditions': ['Sunny', 'Partly Cloudy', 'Clear', 'Warm']},
}


@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Query parameter: city (required)
    Example: /weather?city=New York
    """
    city = request.args.get('city')
    
    if not city:
        return jsonify({
            'error': 'City parameter is required',
            'example': '/weather?city=New York'
        }), 400
    
    if city not in WEATHER_DATA:
        return jsonify({
            'error': f'Weather data not available for {city}',
            'available_cities': list(WEATHER_DATA.keys())
        }), 404
    
    # Generate random weather data
    city_data = WEATHER_DATA[city]
    temperature = random.randint(city_data['temp_range'][0], city_data['temp_range'][1])
    condition = random.choice(city_data['conditions'])
    humidity = random.randint(30, 90)
    wind_speed = random.randint(0, 25)
    
    weather_info = {
        'city': city,
        'temperature': temperature,
        'temperature_unit': 'Fahrenheit',
        'condition': condition,
        'humidity': f'{humidity}%',
        'wind_speed': f'{wind_speed} mph',
        'timestamp': datetime.now().isoformat()
    }
    
    return jsonify(weather_info), 200


@app.route('/weather/cities', methods=['GET'])
def get_cities():
    return jsonify({
        'available_cities': list(WEATHER_DATA.keys())
    }), 200


@app.route('/', methods=['GET'])
def home():
    """
    Home endpoint with API information.
    """
    return jsonify({
        'service': 'Weather Microservice',
        'version': '1.0',
        'endpoints': {
            '/weather': 'GET weather data for a city (requires ?city= parameter)',
            '/weather/cities': 'GET list of available cities'
        },
        'example': '/weather?city=New York'
    }), 200


if __name__ == '__main__':
    print("Starting Weather Microservice on port 5055...")
    print("Available endpoints:")
    print("  - GET /weather?city=<city_name>")
    print("  - GET /weather/cities")
    print("  - GET /")
    app.run(host='0.0.0.0', port=5055, debug=True)
