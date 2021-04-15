from typing import List, Tuple
import requests
import json
from datetime import datetime, timedelta
import re

class WeatherApi:
    def __init__(self):
        self.link = 'https://www.worldweatheronline.com'
        self.wind_directions = {
            'N': 0,
            'NNE': 25, 'NE': 45, 'ENE': 65, 'E': 90,
            'ESE': 115, 'SE': 135, 'SSE': 155, 'S': 180,
            'SSW': 205, 'SW': 225, 'WSW': 245, 'W': 270,
            'WNW': 295, 'NW': 320, 'NNW': 345}


    def get_wind_direction(self, url, day: datetime):
        date = day.strftime('%Y-%m-%d')
        data = {'ctl00$MainContentHolder$txtPastDate': date,
                'ctl00$MainContentHolder$butShowPastWeather': 'Get+Weather',
                'ctl00$rblTemp': 1,
                'ctl00$rblPrecip': 1,
                'ctl00$rblWindSpeed': 2,
                'ctl00$rblheight': 1,
                'ctl00$hdlat': '',
                'ctl00$hdlon': "",
                '__VIEWSTATEGENERATOR':	"",
                '__VIEWSTATE': '',
                'ctl00$areaid': 1,
                'ctl00$rblVis': 1
                }
        query = requests.post(url, data=data)
        text = query.text
        winds = re.findall(r'\d{1,3} km/h from \w{1,3}', text)
        if not winds:
            return
        directions = list(map(lambda x: x.split()[-1], winds))[:9]
        direction = int(sum(map(lambda x: self.wind_directions[x], directions)) / len(directions))

        deg_now = 361
        dir_now = ''
        for key, val in self.wind_directions.items():
            if abs(val - direction) < deg_now:
                deg_now = abs(val - direction)
                dir_now = key
        return dir_now

    def get_wind_during_date(self, url, datefrom:datetime, dateto:datetime):
        days = dateto - datefrom
        data = []
        for i in range(1, days.days):
            date = dateto - timedelta(days=i)
            data.append(self.get_wind_direction(url, date))
        return data


    def get_city(self, name):
        data = requests.get(f'https://www.worldweatheronline.com/v2/search.ashx?qry={name}')
        return data.json()
