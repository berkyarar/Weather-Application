import tkinter
import requests
from datetime import datetime, timezone
from tkinter import messagebox

window = tkinter.Tk()
window.minsize(400, 400)
window.title("Weather Forecast")
window.config(background="pink")
window.config(padx=10, pady=10)

api_key = "c0c2210aca0ea8ae0211b1feff3d4eb1"

city_value = tkinter.StringVar()


def show_weather():
    try:
        city_input = city_value.get()

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            country = data["sys"]["country"]
            temp = (data["main"]["temp"]) - 273.15
            feels_like = (data["main"]["feels_like"]) - 273.15
            desc = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            sunrise = data['sys']['sunrise']
            sunset = data['sys']['sunset']
            timezone = data['timezone']

            sunrise_time = time_format_for_location(sunrise + timezone)
            sunset_time = time_format_for_location(sunset + timezone)

            weather_info = f"Country code: {country}\n City name : {city_input}\n Temperature(celcius): {round(temp)}\n Felt temperature(celcius): {round(feels_like)}\n Description: {desc}\n Wind speed(m/s): {wind_speed}\n Sunrise: {sunrise_time}\n Sunset: {sunset_time} "
            weather_result_label.config(text=weather_info, font=("arial", 15, "bold"))

            return

        elif city_input not in response.json():
            messagebox.showinfo(title="Error!", message="invalid city name!")
            weather_result_label.config(text="")

        else:
            messagebox.showinfo(title="Error!", message="Unable to retrieve weather data")
    except requests.exceptions.ConnectionError:
        messagebox.showinfo(title="Error!", message="connection error please check your network connection.")


def time_format_for_location(utc_with_tz):
    local_time = datetime.fromtimestamp(utc_with_tz, tz=timezone.utc)
    return local_time.time()


city_label = tkinter.Label(text="CİTY NAME", font=("arial", 15, "normal"), background="pink")
city_label.config(padx=10, pady=10)
city_label.pack()

city_entry = tkinter.Entry(width=30, textvariable=city_value)
city_entry.pack()

result_button = tkinter.Button(text="Weather Results", command=show_weather, background="#D3C6CD",foreground="black",font=("arial",10,"bold"))
result_button.config(padx=10, pady=10)
result_button.place(x=125, y=90)

weather_result_label = tkinter.Label(background="pink")
weather_result_label.place(x=50, y=150)


def update_clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)


clock_label = tkinter.Label(font=("arial", 15, "normal"), background="pink")
clock_label.place(x=-8, y=360)

update_clock()
window.mainloop()
