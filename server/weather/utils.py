from const.const import contries_cities


def parsing_params(params):
    pass


def cmp_inputs(input_country, input_city):
    input_country = input_country.replace(" ", "").strip().lower()
    input_city = input_city.replace(" ", "").strip().lower()
    
    for country, cities in contries_cities.items():
        processed_country = country.replace(" ", "").strip().lower()
        
        if processed_country == input_country:
            for city in cities.keys():
                processed_city = city.replace(" ", "").strip().lower()
                
                if input_city == processed_city:
                    return country, city
    
    
if __name__ == "__main__":
    input_country = "south korea"
    input_city = "kwangju"
    
    country, city = cmp_inputs(input_country, input_city)
    print(country, city)