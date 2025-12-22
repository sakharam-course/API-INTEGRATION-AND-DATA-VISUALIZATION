# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SAKHARAM SAWANT

*INTERN ID*: CT04DR2481

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH



TASK 1 : API-INTEGRATION-AND-DATA-VISUALIZATION

-Project Description

This project focuses on **API Integration and Data Visualization** using Python. The application integrates with the **OpenWeatherMap API** to fetch real-time weather forecast data for a selected city (Delhi) and visualizes key weather parameters such as **temperature, humidity, and atmospheric pressure** using graphical charts.

The purpose of this task is to demonstrate how external REST APIs can be accessed programmatically, how JSON data can be processed and structured using data analysis tools, and how meaningful insights can be presented through clear and effective visualizations.

- Objectives

* Integrate a third-party API using Python
* Fetch real-time weather forecast data
* Process and structure API response data
* Perform basic data handling using pandas
* Visualize weather data using Matplotlib and Seaborn
* Create a simple weather dashboard

- API Used

**OpenWeatherMap – 5 Day / 3 Hour Forecast API**

* Provides weather forecast data in 3-hour intervals
* Returns data in JSON format
* Widely used in real-world weather applications

**API Endpoint:**

```
https://api.openweathermap.org/data/2.5/forecast
```

**Parameters Used:**

* `q` → City name (Delhi)
* `appid` → API key
* `units` → Metric (Celsius)

- Technologies Used

* **Python**
* **Requests** – For API communication
* **Pandas** – For data processing and manipulation
* **Matplotlib** – For plotting graphs
* **Seaborn** – For styling visualizations

-How the Project Works

1. The program sends a request to the OpenWeatherMap API using the `requests` library.
2. The API responds with weather forecast data in JSON format.
3. Important weather parameters are extracted from the response:

   * Date & Time
   * Temperature (°C)
   * Humidity (%)
   * Atmospheric Pressure (hPa)
4. The extracted data is stored in a pandas DataFrame.
5. The DateTime column is converted to a datetime format for accurate plotting.
6. The data is visualized using three separate line graphs arranged in a single dashboard.

- Data Visualization

The project generates a **three-plot weather dashboard**:

- Temperature Forecast

* Displays temperature variations over time
* Represented using a red line plot
* Helps identify daily temperature trends

- Humidity Forecast

* Displays humidity percentage changes
* Represented using a blue line plot
* Useful for understanding atmospheric moisture levels

- Pressure Forecast

* Displays atmospheric pressure variations
* Represented using a green line plot
* Indicates weather stability or changes

All plots share a common Date & Time axis, allowing easy comparison of weather parameters.

---

- Output

The final output is a **graphical dashboard** showing:

* Temperature (°C)
* Humidity (%)
* Pressure (hPa)

across multiple forecast timestamps for the city of Delhi.

The output is displayed using Matplotlib and matches the provided screenshot.

---

- How to Run the Project

1. Install required libraries:

```bash
pip install requests pandas matplotlib seaborn
```

2. Replace the API key in the code with your own OpenWeatherMap API key.

3. Run the Python script:

```bash
python weather_dashboard.py
```

4. The weather visualization dashboard will be displayed on the screen.

- Conclusion

This project successfully demonstrates **API Integration and Data Visualization** by combining real-time weather data with Python-based visualization tools. It highlights how external APIs can be used to fetch live data, process it efficiently, and present it in an understandable visual format. This task is a practical example of real-world data handling and visualization techniques used in modern applications.



*OUTPUT*: <img width="1919" height="1018" alt="Image" src="https://github.com/user-attachments/assets/f9202c90-a71b-4ebc-88ff-9ba8f38df4ca" />
