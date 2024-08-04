from datetime import datetime
from collections import defaultdict

from meteostat import Monthly, Point, Stations

from const.const import contries_cities


def get_city_suggestion(start_month: int, end_month: int):
    year = datetime.now().year
    query_start = datetime(year - 1, start_month, 1)
    query_end = datetime(year - 1, end_month, 1)
    
    weather_stations = Stations()
    stations = defaultdict(dict)
    for country in contries_cities.keys():
        for city, (lat, long) in contries_cities[country].items():
            weather_stations = weather_stations.nearby(lat, long)
            stations[country][city] = weather_stations.fetch(1)
    
    datas = defaultdict(lambda: defaultdict(dict))
    inter_cols = ["time", "tavg", "tmin", "tmax", "prcp", "tsun"]
    for country in stations.keys():
        for city, station in stations[country].items():
            data = Monthly(station, query_start, query_end).fetch()
            data = data.fillna("")
            for time, weather in data.to_dict("index").items():
                datas[country][city][str(time)[:7]] = weather
                
    return datas
    
    
def get_specific_weather(country, city, start_month, end_month):
    year = datetime.now().year
    query_start = datetime(year - 1, start_month, 1)
    query_end = datetime(year - 1, end_month, 1)
    
    weather_stations = Stations()
    station = weather_stations.nearby(contries_cities[country][city][0], contries_cities[country][city][1]).fetch(1)
    
    datas = defaultdict(lambda: defaultdict(dict))
    data = Monthly(station, query_start, query_end).fetch()
    data = data.fillna("")
    for time, weather in data.to_dict("index").items():
        datas[country][city][str(time)[:7]] = weather
    
    return datas
