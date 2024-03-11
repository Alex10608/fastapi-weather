from datetime import datetime


"""Функция для обработки ответа от Openweathermap, 
он возвращает слишком много параметров, функция возвращает только необходимые"""

def custom_weather_data(data: dict) -> dict:
    forecast = {}

    for item in data['list']:
        my_date, my_time = datetime.fromtimestamp(item['dt']).strftime('%d.%m.%Y %H:%M').split()
        forecast.setdefault(my_date, {})
        forecast[my_date].setdefault('time', []).append(my_time)
        forecast[my_date].setdefault('temp', []).append(item['main']['temp'])
        forecast[my_date].setdefault('weather', []).append(item['weather'][0]['main'])

    res = {
        "сity": data['name'],
        "temp": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "pressure": data['main']['pressure'],
        "wind_speed": data['wind']['speed'],
        "forecast": forecast
    }
    return res