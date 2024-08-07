# Weather API
___
A simple weather API built with Flask that interacts with an SQLite database and OpenWeatherMap API.

![Screenshot](/Screenshot.png)

___
## API Documentation
[OpenWeatherMap Current Weather Data documentation](https://openweathermap.org/current)

## Features

- Add weather data for a specific city.
- Retrieve weather data for a specific city.
- Web interface using Bootstrap to interact with the API.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Coding-doves/WeatherApp.git
    cd weatherApp
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file or add your API key(get key from  [OpenWeatherMap](https://openweathermap.org/current)) in `Config` class (refer to `config.py`).

5. Run the application:

    ```bash
    python apps/main.py 
    ```
    ```bash
    python apps\main.py # On Windows
    ```

6. Navigate to `http://127.0.0.1:5000` to access the web interface.

## Testing

Run the test cases using:

```bash
python -m unittest test_app
