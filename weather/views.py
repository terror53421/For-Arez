from django.http import HttpResponse
from django.template import loader
import requests
from .weather import get_kiev_weather

 
APPID = "0e34d35ab42a03b8a032b3d39937acbc"
URL_BASE = "https://api.openweathermap.org/data/2.5/"

"""function on main url"""
def weather(request):
    template = loader.get_template('main.html')
    context = {
        'weather': get_kiev_weather(),
    }
    return HttpResponse(template.render(context,request))


