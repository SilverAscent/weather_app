# main.py

from weather_api import get_weather
from file_manager import read_cities, save_weather_to_file, log_summary

def main():
    cities = read_cities('cities.txt')
    for city in cities:
        data = get_weather(city)
        if data:
            save_weather_to_file(city, data)
            log_summary(city, data)
            print(f"{city}: {data['main']['temp']}°C,{data['weather'][0]['description']}")
            print(f"Humidity from {data['name']}: {data['main']['humidity']}")
            print(f"Wind speed from {data['name']}: {data['wind']['speed']}")
if __name__ == "__main__":
    main()