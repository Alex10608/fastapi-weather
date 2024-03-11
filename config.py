from dataclasses import dataclass

from environs import Env


@dataclass
class Weather:
    api_key: str
    url_current: str
    url_forecast: str


@dataclass
class Config:
    weather: Weather


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(weather=Weather(
        api_key=env("API_KEY"),
        url_current=env("URL_FOR_CURRENT"),
        url_forecast=env("URL_FOR_FORECAST"),
    )
)
