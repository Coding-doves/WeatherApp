import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///weather.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WEATHER_API_KEY = os.environ['current_weather_api_key']  # api key from OpenWeather Map website
