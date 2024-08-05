from datetime import datetime
import unittest
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from apps.main import app, db  

class TestWeather(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the test environment."""
        cls.app = app
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

        cls.client = cls.app.test_client()
        cls.db = db
        cls.db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Clean up after tests."""
        cls.db.session.remove()
        cls.db.drop_all()
        cls.app_context.pop()

    def test_add_weather(self):
        """Test adding weather data."""
        response = self.client.post('/weather', json={
            'city': 'Delhi',
            'date': datetime.now().date().isoformat(),
            'temperature': 24,
            'description': 'Delhi weather'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Weather data added successfully!", response.data)

    def test_get_weather(self):
        """Test retrieving weather data."""
        # First, add some weather data
        self.client.post('/weather', json={
            'city': 'Abuja',
            'date': datetime.now().date().isoformat(),
            'temperature': 20,
            'description': 'Abuja weather'
            })
    
        # Now retrieve it
        response = self.client.get('/weather/Abuja')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Abuja", response.data)
    
    def test_add_open_weather(self):
        """Test adding weather data."""
        response = self.client.post('/open_weather', json={
            'city': 'London'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Weather data added successfully!", response.data)
    
    def test_get_open_weather(self):
        """Test retrieving weather data."""
        # First, add some weather data
        self.client.post('/open_weather', json={
            'city': 'Paris'})
        
        # Now retrieve it
        response = self.client.get('/weather/Paris')
        self.assertEqual(response.status_code, 200)
        
        response_data = response.get_json()
        print(response_data)  # Print response data to inspect it

        self.assertEqual(response_data[0]['city'], 'PARIS')


if __name__ == '__main__':
    unittest.main()
