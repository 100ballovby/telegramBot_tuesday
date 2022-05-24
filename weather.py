import requests as r
import json


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {  # параметры для запроса
        'q': city.capitalize(),  # Пишет город с большой буквы
        'appid': '',
        'units': 'metric',  # градусы в цельсиях
        'lang': 'ru'  # русский язык
    }
    response = r.get(url, params=params)
    return response.json()  # возвращаю ответ сервера в JSON формате

with open('weather.json', 'w') as file:
    w = get_weather('Минск')
    file.write(json.dumps(w))
