import requests
import os
from dotenv import load_dotenv

load_dotenv()
def get(city, days, kind):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={os.environ.get("API_OPENWEATHER")}")
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        temperatures = [item["main"]["temp"] for item in filtered_data]
        dates = [item["dt_txt"] for item in filtered_data]
        return temperatures, dates
    elif kind == "Sky":
        return [item["weather"][0]["description"] for item in filtered_data]
    else:
        return "Invalid kind"
