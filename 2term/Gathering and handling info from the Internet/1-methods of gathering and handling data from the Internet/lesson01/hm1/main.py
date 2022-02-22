import requests
import json
import os

# 1
res = requests.get(f'https://api.github.com/users/alex-coch/repos')
with open('les1.json', 'w') as f:
    json.dump(res.json(), f)
for item in res.json():
    print(item['name'])

# 2
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
weather_params = {
    "lat": "50",
    "lon": "50",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
with open('les1.2.json', 'w') as f:
    json.dump(weather_data, f)