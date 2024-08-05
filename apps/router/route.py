from datetime import datetime
from config import Config
from model import db, Weather
from flask import Blueprint, request, jsonify, render_template
import requests


# Initialize
routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Store weather data in db
@routes.route('/weather', methods=['POST'])
def add_weather():
    try:
        data = request.get_json()
        city = data.get('city').upper()
        date = data.get('date')
        temperature = data.get('temperature')
        description = data.get('description')

        # Convert date string to datetime.date object
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"message": "Date format should be YYYY-MM-DD"}), 400

        # Ensure temperature is a float
        try:
            temperature = float(temperature)
        except ValueError:
            return jsonify({"message": "Temperature must be a valid number"}), 400

        new_weather = Weather(
            city=city,
            date=date,
            temperature=temperature,
            description=description
        )

        db.session.add(new_weather)
        db.session.commit()
        return jsonify({"message": "Weather data added successfully!"}), 201

    except Exception as e:
        return jsonify({"message": e})


# Fetch weather data from API if city is provided but not complete details
@routes.route('/open_weather', methods=['POST'])
def weather_from_api():
    try:
        data = request.get_json()
        city = data.get('city', '').upper()
        # print(city)

        if city:
            # API key from config.py
            KEY = Config.WEATHER_API_KEY
            weather_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+KEY
            response = requests.get(weather_api_link)
            weather_data = response.json()
            # print(weather_data)

            if response.status_code != 200:
                return jsonify({"message": "Error retrieving weather data"}), 400

            date=datetime.now().date()
            temperature=((weather_data['main']['temp']) - 273.15) # convert kelvin to celsius
            description=weather_data['weather'][0]['description']
            new_weather = Weather(
                city=city,
                date=date,
                temperature=temperature,
                description=description
            )
        else:
            return jsonify({"message": "Insufficient data provided"}), 400

        db.session.add(new_weather)
        db.session.commit()
        return jsonify({"message": "Weather data added successfully!"}), 201

    except Exception as e:
        return jsonify({"message": e})
        
# Read stored data
@routes.route("/weather/<string:city>", methods=['GET'])
def read_weather(city):
    city = city.upper()
    db_weather = Weather.query.filter_by(city=city).all()
    if not db_weather:
        return jsonify({"message": f"{city} city not found!"}), 404
    
    return jsonify([{
        "id": v.id,
        "city": v.city,
        "date": v.date.strftime('%d %b %Y | %I:%M:%S %p'),
        "temperature": f"{v.temperature:.2f}",
        "description": v.description}
        for v in db_weather])
