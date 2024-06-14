import requests
import os
from dotenv import load_dotenv

load_dotenv()
def get(city, days, kind, unit="Kelvin"):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={os.environ.get("API_OPENWEATHER")}")
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    
    dates = [item["dt_txt"] for item in filtered_data]
    
    if kind == "Temperature":
        if unit == "Celcius":
            temperatures = [item["main"]["temp"] - 273.15 for item in filtered_data]
        else:
            temperatures = [item["main"]["temp"] for item in filtered_data]
        return temperatures, dates
    
    elif kind == "Sky":
        sky_condition = [item["weather"][0] for item in filtered_data]
        return sky_condition, dates
    else:
        return "Invalid kind"

get("Montevideo", 2, "Temperature")
