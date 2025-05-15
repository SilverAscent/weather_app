from tkinter import ttk
from tkinter import *
from weather_api import get_weather
from file_manager import read_cities, save_weather_to_file, log_summary
def submit():
    with open('cities.txt',"a") as file:
        file.write(city_entry.get())
root=Tk()
root.title("Weather Form")
Label(root, text="Enter the city:").pack()
city_entry = Entry(root)
city_entry.pack()
Button(root,text="Get Weather",command=submit).pack()
root.mainloop()
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