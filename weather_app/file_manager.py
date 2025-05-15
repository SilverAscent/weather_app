

import json
def read_cities(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def save_weather_to_file(city, data):
    filename = f"{city.lower().replace(' ', '_')}_weather.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def log_summary(city, data):
    with open("weather_summary.txt", "a") as file:
        summary = f"{city}: {data['main']['temp']}°C,{data['weather'][0]['description']}\nHumidity from {data['name']}: {data['main']['humidity']}\nWind speed from {data['name']}: {data['wind']['speed']}"
        file.write(summary)