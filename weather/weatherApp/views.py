from django.shortcuts import render
from django.http import HttpResponse
import json 
import urllib.request 
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        source = urllib.request.urlopen( 
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1e2b1c4a18787d3b51e6b5070e19d4de').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        if not list_of_data:
            return HttpResponse("Nothing")
        else:
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
            return render(request, 'weather.html', {'country_code':country_code, 'coordinate':coordinate, 'temp':temp, 'pressure':pressure, 'humidity':humidity})
    else:
        data = {} 
        return render(request, 'weather.html')

            #return render(request, 'weather.html', {'country_code':country_code, 'coordinate':coordinate, 'temp':temp, 'pressure':pressure, 'humidity':humidity})


def county_weather(request):
    counties = ['lamu', 'meru', 'nairobi', 'nyeri', 'nakuru']
    temps = [0, 0, 0, 0, 0]
    for i in range(0, len(counties)):
        source = urllib.request.urlopen( f'http://api.openweathermap.org/data/2.5/weather?q={counties[i]}&appid=1e2b1c4a18787d3b51e6b5070e19d4de').read() 
        list_of_data = json.loads(source)
        data = {
        "temp" : str(list_of_data['main']['temp']) +  'k',
        } 
        temps[i] = data['temp']

    print(temps[0], temps[1])
    lamu_temp = temps[0];meru_temp = temps[1];nairobi_temp = temps[2]; nyeri_temp = temps[3]; nakuru_temp = temps[4]

    return render(request, 'county_weather.html', {'lamu_temp':lamu_temp, 'meru_temp':meru_temp, 'nairobi_temp':nairobi_temp, 'nyeri_temp':nyeri_temp, 'nakuru_temp':nakuru_temp})

@api_view(['GET','POST', 'DELETE'])
def weather_api(request):
    counties = ['lamu', 'meru', 'nairobi', 'nyeri', 'nakuru']
    temps = [0, 0, 0, 0, 0]
    for i in range(0, len(counties)):
        source = urllib.request.urlopen( f'http://api.openweathermap.org/data/2.5/weather?q={counties[i]}&appid=1e2b1c4a18787d3b51e6b5070e19d4de').read() 
        list_of_data = json.loads(source)
        data = {
        "temp" : str(list_of_data['main']['temp']) +  'k',
        } 
        temps[i] = data['temp']
    lamu_temp = temps[0];meru_temp = temps[1];nairobi_temp = temps[2]; nyeri_temp = temps[3]; nakuru_temp = temps[4]
    data = {
        "lamu_temp":lamu_temp,
        "meru_temp":meru_temp,
        "nairobi_temp":nairobi_temp,
        "nyeri_temp":nyeri_temp,
        "nakuru_temp":nakuru_temp,
    }
    if request.method == 'GET':
        return Response(data)
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass

    #return HttpResponse(json.dumps(data), content_type='application/json')

def weather_graph(request):
    return render(request, 'weather_graph.html')