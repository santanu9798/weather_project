
import requests
from django.shortcuts import render
from django.conf import settings


def index(request):
    weather_data = None
    error = None
    city = ''

    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:
            api_key = 'a643ee362f026b3b63010fee2e9ab040'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    weather_data = {
                        'city': data['name'],
                        'temperature': round(data['main']['temp']),
                        'description': data['weather'][0]['description'],
                        'icon': data['weather'][0]['icon'],
                        'humidity': data['main']['humidity'],
                        'wind_speed': data['wind']['speed'],
                        'feels_like': round(data['main']['feels_like']),
                    }
                elif response.status_code == 404:
                    error = f'City "{city}" not found. Please try again.'
                else:
                    error = 'Unable to fetch weather data. Please check your API key.'
            except requests.exceptions.ConnectionError:
                error = 'No internet connection. Please try again.'
            except requests.exceptions.Timeout:
                error = 'Request timed out. Please try again.'
            except Exception as e:
                error = 'Something went wrong. Please try again.'

    context = {
        'weather_data': weather_data,
        'error': error,
        'city': city,
    }
    return render(request, 'weather_app/index.html', context)