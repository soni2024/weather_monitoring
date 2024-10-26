# Real-Time Data Processing System for Weather Monitoring

## Overview

This project is a real-time data processing system developed to monitor weather conditions and provide summarized insights using rollups and aggregates. The system retrieves data from the OpenWeatherMap API and processes it to offer meaningful insights.

## Features

- **Real-time Data Retrieval**: Continuously fetches weather data from OpenWeatherMap for key metros in India.
- **Data Aggregation**: Provides daily weather summaries with average, maximum, and minimum temperatures, and dominant weather conditions.
- **Alerts**: Generates alerts based on user-configurable thresholds for temperature and weather conditions.
- **Visualization**: Displays daily summaries and historical trends using an intuitive web interface.
- **Email Notifications**: Sends alerts via email when thresholds are breached.

## Project Structure

weather_monitoring_project/ │ ├── manage.py # Django management script ├── db.sqlite3 # SQLite database (if using SQLite) │ ├── my_rule_engine/ # Main project directory │ ├── init.py │ ├── settings.py # Project settings │ ├── urls.py # Project URLs │ ├── wsgi.py # WSGI entry point for deployment │ ├── weather/ # Application directory for the weather monitoring system │ ├── init.py │ ├── admin.py # Admin interface for models │ ├── apps.py # Application configuration │ ├── migrations/ # Directory for migration files │ ├── models.py # Database models │ ├── tests.py # Unit tests for the application │ ├── urls.py # Application-specific URLs │ ├── views.py # View functions for handling requests │ ├── serializers.py # Serializers for converting data to/from JSON │ ├── ast.py # AST logic for rule parsing and evaluation │ ├── forms.py # Forms for user input (if needed) │ ├── templates/ # Directory for HTML templates │ │ ├── base.html # Base template │ │ ├── index.html # Homepage template │ │ ├── rule_form.html # Template for rule input form │ │ ├── combine_rules.html# Template for combining rules │ │ ├── evaluation_result.html # Template for displaying evaluation results │ ├── management/ # Management commands for data fetching and processing │ │ ├── init.py │ │ └── commands/ │ │ ├── fetch_weather_data.py │ │ ├── summarize_weather_data.py │ │ ├── check_alerts.py │ └── requirements.txt # Required packages for the project



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/soni2024/weather_monitoring.git
git branch -M main
git push -u origin main
    cd weather_monitoring_project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

### Fetch Weather Data

1. Run the `fetch_weather_data` command to fetch weather data from the OpenWeatherMap API:
    ```bash
    python manage.py fetch_weather_data
    ```

### Summarize Weather Data

1. Run the `summarize_weather_data` command to create daily summaries:
    ```bash
    python manage.py summarize_weather_data
    ```

### Check Alerts

1. Run the `check_alerts` command to check for weather alerts based on thresholds:
    ```bash
    python manage.py check_alerts
    ```

### Access the Web Interface

1. Navigate to `http://127.0.0.1:8000/` to access the homepage and view weather summaries and alerts.

### Run Tests

1. Run unit tests to ensure everything works as expected:
    ```bash
    python manage.py test
    ```

## Dependencies

Ensure you have the following dependencies installed. These are listed in the `requirements.txt` file:

- Django
- requests
- djangorestframework

## Contributing

Feel free to open issues or submit pull requests for any improvements or bug fixes.
