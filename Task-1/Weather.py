import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "c768aa5c40c3393728b195819672d4ba"  # REPLACE API KEY
CITY = "Delhi"

# OpenWeatherMap API URL
URL = "https://api.openweathermap.org/data/2.5/forecast"

# PARAMETERS
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"   # Temperature in Celsius
}

# FETCH WEATHER DATA
response = requests.get(URL, params=params)

if response.status_code != 200:
    print("Error fetching data:", response.text)
    exit()

data = response.json()

# PARSE DATA INTO DATAFRAME
weather_records = []

for item in data["list"]:
    weather_records.append({
        "DateTime": item["dt_txt"],
        "Temperature": item["main"]["temp"],
        "Humidity": item["main"]["humidity"],
        "Pressure": item["main"]["pressure"]
    })

# Create DataFrame
df = pd.DataFrame(weather_records)
df["DateTime"] = pd.to_datetime(df["DateTime"])


# CREATE VISUALIZATION DASHBOARD
sns.set(style="darkgrid")  

plt.figure(figsize=(12, 8))


# Temperature Plot
plt.subplot(3, 1, 1)
plt.plot(df["DateTime"], df["Temperature"], color='red', marker='o')
plt.title(f"{CITY} Weather Forecast")
plt.ylabel("Temperature (°C)")

# Humidity Plot
plt.subplot(3, 1, 2)
plt.plot(df["DateTime"], df["Humidity"], color='blue', marker='o')
plt.ylabel("Humidity (%)")

# Pressure Plot
plt.subplot(3, 1, 3)
plt.plot(df["DateTime"], df["Pressure"], color='green', marker='o')
plt.ylabel("Pressure (hPa)")
plt.xlabel("Date & Time")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()






