# fastapi-weather
API для приложения погоды, работает с сервером OpenWeatherMap.
Для корректной работы нужно:
 - установить Redis
 - клонировать репозиторий
 - установить зависимости pip instal -r requirements.txt
 - зарегистрироваться на https://openweathermap.org и получить API Key
 - в файле .env указать свой API Key в поле API_KEY
 - запустить приложение командой uvicorn main:app --reload
