# Weather Forecast App (Tkinter + OpenWeatherMap API)

This project is a simple **desktop weather forecast application** built with Tkinter.  
It fetches real-time weather data from the **OpenWeatherMap API** and displays information such as temperature,
description, wind speed, and sunrise/sunset times.

---

## 📌 Features

- User-friendly Tkinter GUI
- Get weather data by city name
- Displays:
    - Country code and city name
    - Temperature and "feels like" temperature (°C)
    - Weather description
    - Wind speed
    - Sunrise and sunset times (local)
- Real-time digital clock inside the app
- Error handling for invalid city names and connection issues

---

## 🛠️ Tech Stack
  
- Python
- Tkinter (GUI)
- Requests (HTTP requests to OpenWeatherMap API)
- Datetime (time formatting)

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/username/weather-forecast-app.git
   cd weather-forecast-app

2. Install requirements:
   pip install -r requirements.txt

3. Run the app:
   python main.py

🔑 API Key

This app uses the OpenWeatherMap API

Sign up and get your free API key.

Replace the api_key variable in the script with your own key:

api_key = "YOUR_API_KEY"

