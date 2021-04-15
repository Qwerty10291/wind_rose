from typing import List
from sqlalchemy import and_
from db_session import *
from models import *
from weather_api import WeatherApi
from datetime import datetime, timedelta

class Data:
    def __init__(self, filename='db.sqlite') -> None:
        self.filename = filename
        global_init(filename)
        self.weather = WeatherApi()
    
    def search_city(self, name):
        session = create_session()
        cities = self.weather.get_city(name)
        data = map(lambda x: x.title, session.query(City).all())
        filtered = filter(lambda x: x['name'] not in data, cities)
        return list(filtered)
    
    def add_city(self, data:dict):
        session = create_session()
        city = City()
        city.title = data['name']
        city.link = self.weather.link + data['url'].replace('weather', 'weather-history')
        session.add(city)
        session.commit()

    def load_cities(self) -> List[City]:
        session = create_session()
        cities = session.query(City).all()
        return cities
    
    def load_weather(self, date_from:datetime, date_to:datetime, city:City) -> List[str]:
        session = create_session()
        data = []
        url = city.link
        winds = session.query(Winds).filter(
            and_(Winds.date >= date_from.strftime('%Y-%m-%d'), Winds.date <= date_to.strftime('%Y-%m-%d'))).all()
        if len(winds) == 0:
            days = date_to.__sub__(date_from).days
            for i in range(1, days):
                date = date_to - timedelta(days=i)
                direction = self.weather.get_wind_direction(url, date)
                if not direction:
                    continue
                data.append(direction)
                wind = Winds()
                wind.date = date
                wind.city_id = city.id
                wind.wind = direction
                session.add(wind)
                session.commit()
        else:
            data = list(map(lambda x: x.wind, winds))
            db_date_from = min(list(map(lambda x: x.date, winds)))
            days = db_date_from.__sub__(date_from).days
            for i in range(1, days):
                date = db_date_from - timedelta(days=i)
                direction = self.weather.get_wind_direction(url, date)
                if not direction:
                    continue
                data.append(direction)
                wind = Winds()
                wind.date = date
                wind.city_id = city.id
                wind.wind = direction
                session.add(wind)
                session.commit()
        return data