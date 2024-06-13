import requests
import os
from dotenv import load_dotenv

load_dotenv()
def get(city, ):
    response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={os.environ.get("API_OPENWEATHER")}")
    return response.json()

""
    