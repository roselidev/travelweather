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
    
    
def get_specific_weather(country, city, start_month, end_month, years=10):
    def get_comment(good_score):
        if good_score > 0.8:
            return "Perfect days for travel! 🤞"
        elif good_score > 0.2:
            return "There might be a few rainy days, but still a great trip :D"
        else:
            return "Challenging days for travel! But it will still be memorable."

    def get_emoji(prcp):
        if prcp < 30:
            return "fa fa-sun"
        elif prcp < 50:
            return "fa fa-cloud"
        else:
            return "fa fa-cloud-rain"
    
    datas = defaultdict(lambda: defaultdict(float))
    year = datetime.now().year

    # Fetch weather data for the last 3 years
    for i in range(1, years+1):
        query_start = datetime(year - i, start_month, 1)
        query_end = datetime(year - i, end_month, 28)  # Last day of the end month, 28 is safe for all months
    
        weather_stations = Stations()
        station = weather_stations.nearby(contries_cities[country][city][0], contries_cities[country][city][1]).fetch(1)
    
        data = Monthly(station, query_start, query_end).fetch()
        data = data.fillna(0)  # Fill missing data with 0
        
        for index, row in data.iterrows():
            month = index.month
            datas[month]['tavg'] += row['tavg']
            datas[month]['tmin'] += row['tmin']
            datas[month]['tmax'] += row['tmax']
            datas[month]['prcp'] += row['prcp']

    good_score = 0
    for month in range(start_month, end_month + 1):
        tavg = datas[month]['tavg'] / years
        tmin = datas[month]['tmin'] / years
        tmax = datas[month]['tmax'] / years
        prcp = datas[month]['prcp'] / years
        
        datas[month] = {
            'tavg': tavg,
            'tmin': tmin,
            'tmax': tmax,
            'prcp': prcp,
            'emoji': get_emoji(prcp)
        }

        if prcp < 30:
            good_score += 1
        elif prcp < 50:
            good_score += 0.3
        else:
            good_score += 0.1
    
    good_score /= (end_month - start_month + 1)

    datas['comment'] = get_comment(good_score)
        
    return dict(datas)
