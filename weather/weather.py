import requests



APPID = "0e34d35ab42a03b8a032b3d39937acbc"
URL_BASE = "https://api.openweathermap.org/data/2.5/"


def get_kiev_weather():
    params = dict(q="Kyiv", appid= APPID, units= "metric", lang= "ua")
    response = requests.get(URL_BASE + "weather", params=params)
    weather_list = response.json()
    if response.status_code == 200:
        return weather_list['main']['temp']
    else:
        return None
    


