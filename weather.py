import requests as r
import os
from datetime import datetime


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {  # параметры для запроса
        'q': city.capitalize(),  # Пишет город с большой буквы
        'appid': os.environ.get('WEATHER_KEY'),
        'units': 'metric',  # градусы в цельсиях
        'lang': 'ru'  # русский язык
    }
    response = r.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        today = datetime.today()  # сегодняшняя дата и время
        forecast = []  # здесь буду хранить прогнозы
        for line in data['list']:
            date = datetime.fromtimestamp(line['dt'])
            if date.day in [today.day, today.day + 1] or date.day == 1:
                day = {
                    'date': datetime.strftime(date, '%d/%m, %H:%M'),
                    'temp': round(line['main']['temp']),
                    'weather': line['weather'][0]['description']
                }
                forecast.append(day)
        return forecast
    else:
        return None


print(get_weather('Гонолулу'))
