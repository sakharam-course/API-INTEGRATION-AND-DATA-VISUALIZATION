# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SAKHARAM SAWANT

*INTERN ID*: CT04DR2481

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH



TASK 1 : API-INTEGRATION-AND-DATA-VISUALIZATION
- Introduction

This project has been developed as part of the CODTECH Python Programming Internship. The objective of this task is to demonstrate API Integration and Data Visualization using Python. The project involves fetching real-time weather forecast data from an external API and visualizing the data in a clear and meaningful way.

For this implementation, the OpenWeatherMap API has been integrated to retrieve weather forecast information for the city of Delhi. The retrieved data includes temperature, humidity, and atmospheric pressure, which are then processed and visualized using Python data visualization libraries.

API integration and data visualization are essential skills in modern software development and data analytics, as they enable applications to work with live data and present insights in an understandable graphical format.

- Objective

The main objectives of this task are:
--To understand how to integrate third-party APIs using Python
--To fetch real-time weather forecast data from an external source
--To process and structure JSON data efficiently
--To perform data manipulation using pandas
--To visualize multiple data parameters using charts
--To build a simple weather data visualization dashboard

- Tools and Technologies Used

The following tools and libraries were used to complete this task:
Python as the primary programming language
Requests library for API integration and data fetching\
Pandas for data processing and manipulation
Matplotlib for creating data visualizations
Seaborn for enhancing plot styling
Visual Studio Code / Jupyter Notebook for code execution and testing

- Dataset Description

The dataset used in this project is real-time weather forecast data fetched directly from the OpenWeatherMap API. The API provides forecast information at 3-hour intervals for 5 days.
The following weather parameters are extracted from the API response:
Date and Time
Temperature (in Celsius)
Humidity (in percentage)
Atmospheric Pressure (in hPa)
The data is returned in JSON format and converted into a structured pandas DataFrame for easy analysis and visualization.

- API Integration and Implementation

The project begins by sending an HTTP GET request to the OpenWeatherMap Forecast API using the requests library. The API request includes the city name, API key, and unit type (metric).
Once the response is received, the program verifies the request status. If the request is successful, the JSON response is parsed, and the required weather attributes are extracted. These values are stored in a list of dictionaries and later converted into a pandas DataFrame.
The DateTime field is converted into a datetime format to ensure accurate time-series visualization. This structured data is then used for creating graphical plots.

- Data Visualization

The visualization dashboard consists of three line charts, each representing a different weather parameter:

Temperature Forecast
Displays temperature variation over time
Represented using a red line plot
Helps analyze daily temperature trends

Humidity Forecast
Displays humidity percentage changes
Represented using a blue line plot\
Useful for understanding moisture levels

Pressure Forecast
Displays atmospheric pressure variations
Represented using a green line plot
Indicates weather stability and changes

All charts share a common Date & Time axis, making it easy to compare trends across different weather parameters. The visual output matches the provided screenshot.

- Results and Output

The project successfully fetches real-time weather forecast data and visualizes it in an interactive dashboard format. The output displays clear trends for temperature, humidity, and pressure over multiple timestamps.=
A screenshot of the generated visualization has been included in the repository to verify the output and demonstrate successful execution of the program.

- Deliverables

The following files are included in this repository:

weather_dashboard.py
Python script containing API integration, data processing, and visualization logic.

output_screenshot.png
Screenshot showing the weather forecast visualization dashboard.

README.md
Documentation describing the task, implementation, and results.

- Conclusion

This project successfully demonstrates API Integration and Data Visualization using Python. It provides hands-on experience with working on real-time data obtained from an external API, processing structured JSON data, and presenting insights through graphical visualization. The task fulfills the requirements of the CODTECH Python Programming Internship and highlights the practical application of APIs and data visualization techniques in real-world scenarios.

*OUTPUT*: <img width="1919" height="1018" alt="Image" src="https://github.com/user-attachments/assets/f9202c90-a71b-4ebc-88ff-9ba8f38df4ca" />
