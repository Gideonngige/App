from django.shortcuts import render
from django.http import HttpResponse
import json 
import urllib.request 
# Create your views here.

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        if not city:
            city = 'meru'
        source = urllib.request.urlopen( 
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1e2b1c4a18787d3b51e6b5070e19d4de').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data)
        country_code = data['country_code']
        coordinate = data['coordinate']
        temp  = data['temp']
        pressure = data['pressure']
        humidity = data['humidity']
    else:
        data = {} 
        return render(request, 'weather.html')

    return render(request, 'weather.html', {'country_code':country_code, 'coordinate':coordinate, 'temp':temp, 'pressure':pressure, 'humidity':humidity})
