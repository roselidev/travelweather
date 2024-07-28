from datetime import datetime
from collections import defaultdict

from meteostat import Monthly, Point, Stations

from const.const import AIRPORTS


def get_city_suggestion(start_month: int, end_month: int):
    year = datetime.now().year
    query_start = datetime(year - 1, start_month, 1)
    query_end = datetime(year - 1, end_month, 1)
    
    weather_stations = Stations()
    stations = {}
    for iata, (lat, long) in AIRPORTS.items():
        weather_stations = weather_stations.nearby(lat, long)
        stations[iata] = weather_stations.fetch(1)
    
    datas = defaultdict(dict)
    inter_cols = ["time", "tavg", "tmin", "tmax", "prcp", "tsun"]
    for iata, station in stations.items():
        data = Monthly(station, query_start, query_end).fetch()
        data = data.fillna("")
        for time, weather in data.to_dict("index").items():
            print(str(time)[:7])
            print(weather)
            datas[iata][str(time)[:7]] = weather
            
    print(datas)
    
    return datas
    