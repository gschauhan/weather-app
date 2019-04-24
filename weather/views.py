import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=6c684ecff5617a8061e140b19824b98c'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form =  CityForm()
    
    cities = City.objects.all()
    weather_data = []

    for city in cities:
        res = requests.get(url.format(city)).json()        

        city_weather = {
            'city' : city.name,
            'temperature' : res['list'][0]['main']['temp'],
            'description' : res['list'][0]['weather'][0]['description'],
            'icon' : res['list'][0]['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data' : weather_data, 'form' : form}
    print(context)
    return render(request,'weather/weather.html', context)
