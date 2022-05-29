"""
Weather Application App
Enter the city name to find out the weather info of the city.

Tools used: tkinter, requests, API

API used: https://openweathermap.org/current
"""

import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=2601f08b946212363f2c4bc7c0f74f05"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15) # convert to Celsius
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 14400)) # Convert UTC to EST
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 14400))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    label1.config(text = final_info)
    label2.config(text = final_data)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 20, "bold")

textfield = tk.Entry(canvas, font = t) # add an entry to canvas
textfield.pack(pady = 20) # pad y axis
textfield.focus()
textfield.bind('<Return>',getWeather)

label1 = tk.Label(canvas, font = t) # add a label to canvas
label1.pack()
label2 = tk.Label(canvas, font = t) # add a label to canvas
label2.pack()

canvas.mainloop()