from fastapi import FastAPI
import httpx

from utils import custom_weather_data

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from config import Config, load_config

app: FastAPI = FastAPI()
config: Config = load_config()


"""Функция для получения погоды по названию города,
возвращает ответ от API Openweathermap, с фильтром на некоторые параметры """

@app.get("/weather/{location}")
@cache(expire=60)
async def get_weather(location: str):
    payload = {
        "q": location,
        "appid": config.weather.api_key,
        "units": "metric",
    }

    async with httpx.AsyncClient() as client:
        r_now = await client.get(url=config.weather.url_current, params=payload)
        r_forecast = await client.get(url=config.weather.url_forecast, params=payload)
        data = r_now.json() | r_forecast.json()

    if data.get('cod') == '200':
        return custom_weather_data(data)
    return data


"""Запуск Redis'a в качестве хранилища для кэша"""

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="weather-city-cache")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

