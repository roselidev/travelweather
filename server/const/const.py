from collections import defaultdict

import pandas as pd

# # OpenFlights 데이터베이스에서 공항 정보 CSV 파일을 다운로드
# url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"
# cols = ["Airport ID", "Name", "City", "Country", "IATA", "ICAO", "Latitude", "Longitude", "Altitude", "Timezone", "DST", "Tz database time zone", "Type", "Source"]

# # 데이터 로드
# airports_df = pd.read_csv(url, header=None, names=cols)

# # 필요한 열만 선택
# iata_coords_df = airports_df[["IATA", "Name", "City", "Country", "Latitude", "Longitude"]]

# # IATA 코드가 있는 행만 필터링
# iata_coords_df = iata_coords_df[iata_coords_df["IATA"].notnull()]
# iata_coords_df = iata_coords_df[iata_coords_df["IATA"] != "\\N"]

# # CSV 파일로 저장
# iata_coords_df.to_csv("./IATA_codes_with_coordinates.csv", index=False)

iata_codes = pd.read_csv("const/IATA_codes_with_coordinates.csv")

CODES = {}
AIRPORTS = {
    "ITM": (34.785499572753906,135.43800354003906),
    "FUK": (33.585899353027344,130.4510040283203),
    "SHA": (31.197900772094727,121.33599853515624),
    "MFM": (22.149599,113.592003),
    "NAY": (39.78279876708984,116.38800048828124),
    "TPE": (25.0777,121.233002),
    "SIN": (1.35019,103.994003),
    "DAD": (16.043899536132812,108.1989974975586),
    "BKK": (13.681099891662598,100.74700164794922),
    "DXB": (25.2527999878,55.3643989563),
    "LAX": (33.94250107,-118.4079971)
}

for idx, row in iata_codes.iterrows():
    CODES[row["IATA"]] = (row["Latitude"], row["Longitude"], row["Country"], row["City"])


import pandas as pd
from io import StringIO

data = """
Country,IATA,Name,City,Latitude,Longitude
Argentina,COC,Comodoro Pierrestegui Airport,Concordia,-31.296900,-57.996600
Australia,ACF,Brisbane Archerfield Airport,Brisbane,-27.570299,153.007996
Bangladesh,CXB,Cox's Bazar Airport,Cox's Bazar,21.452200,91.963898
Belgium,ANR,Antwerp International Airport (Deurne),Antwerp,51.189400,4.460280
Brazil,CDJ,Conceição do Araguaia Airport,Conceicao Do Araguaia,-8.348350,-49.301498
Bulgaria,BOJ,Burgas Airport,Bourgas,42.569599,27.515200
Cambodia,KZC,Kampong Chhnang Airport,Kompong Chnang,12.255200,104.564003
Canada,YAM,Sault Ste Marie Airport,Sault Sainte Marie,46.485001,-84.509399
Chile,ARI,Chacalluta Airport,Arica,-18.348499,-70.338699
China,PEK,Beijing Capital International Airport,Beijing,40.080101,116.584999
Colombia,AXM,El Eden Airport,Armenia,4.452780,-75.766400
Costa Rica,BAI,Buenos Aires Airport,Buenos Aires,9.163949,-83.330171
Croatia,DBV,Dubrovnik Airport,Dubrovnik,42.561401,18.268200
Cuba,BCA,Gustavo Rizo Airport,Baracoa Playa,20.365299,-74.506203
Denmark,AAR,Aarhus Airport,Aarhus,56.299999,10.619000
Ecuador,ATF,Chachoán Airport,Ambato,-1.212070,-78.574600
Egypt,ALY,El Nouzha Airport,Alexandria,31.183901,29.948900
Fiji,NAN,Nadi International Airport,Nandi,-17.755400,177.442993
Finland,ENF,Enontekio Airport,Enontekio,68.362602,23.424299
France,CQF,Calais-Dunkerque Airport,Calais,50.962101,1.954760
Germany,\\N,Flugplatz Bautzen,Bautzen,51.193611,14.519722
Greece,PYR,Andravida Air Base,Andravida,37.920700,21.292601
Greenland,UAK,Narsarsuaq Airport,Narssarssuaq,61.160500,-45.425999
Guam,UAM,Andersen Air Force Base,Andersen,13.584000,144.929998
Hong Kong,HKG,Hong Kong International Airport,Hong Kong,22.308901,113.915001
Hungary,BUD,Budapest Liszt Ferenc International Airport,Budapest,47.429760,19.261093
Iceland,AEY,Akureyri Airport,Akureyri,65.660004,-18.072701
India,AMD,Sardar Vallabhbhai Patel International Airport,Ahmedabad,23.077200,72.634697
Indonesia,UPG,Hasanuddin International Airport,Ujung Pandang,-5.061630,119.554001
Italy,\\N,Amendola Air Base,Amendola,41.541401,15.718100
Japan,NRT,Narita International Airport,Tokyo,35.764702,140.386002
Laos,LPQ,Luang Phabang International Airport,Luang Prabang,19.897301,102.161003
Macau,MFM,Macau International Airport,Macau,22.149599,113.592003
Madagascar,TNR,Ivato Airport,Antananarivo,-18.796900,47.478802
Malaysia,BTU,Bintulu Airport,Bintulu,3.123850,113.019997
Maldives,MLE,Malé International Airport,Male,4.191830,73.529099
Mexico,ACA,General Juan N Alvarez International Airport,Acapulco,16.757099,-99.753998
Mongolia,ULN,Chinggis Khaan International Airport,Ulan Bator,47.843102,106.766998
Morocco,AGA,Al Massira Airport,Agadir,30.325001,-9.413070
Nepal,BWA,Gautam Buddha Airport,Bhairawa,27.505685,83.416293
Netherlands,AMS,Amsterdam Airport Schiphol,Amsterdam,52.308601,4.763890
New Zealand,AKL,Auckland International Airport,Auckland,-37.008099,174.792007
Norway,AES,Ålesund Airport,Alesund,62.562500,6.119700
Panama,BOC,Bocas Del Toro International Airport,Bocas Del Toro,9.340850,-82.250801
Peru,\\N,Huancabamba Airport,Huancabamba,-5.256770,-79.442902
Philippines,MNL,Ninoy Aquino International Airport,Manila,14.508600,121.019997
Poland,\\N,Babice Airport,Warsaw,52.268501,20.910999
Portugal,AVR,Alverca Air Base,Alverca,38.883301,-9.030100
Puerto Rico,BQN,Rafael Hernandez Airport,Aguadilla,18.494900,-67.129402
Russia,YKS,Yakutsk Airport,Yakutsk,62.093300,129.770996
Saudi Arabia,AHB,Abha Regional Airport,Abha,18.240400,42.656601
Singapore,\\N,Sembawang Air Base,Sembawang,1.425260,103.813004
South Africa,ALJ,Alexander Bay Airport,Alexander Bay,-28.575001,16.533300
South Korea,KWJ,Gwangju Airport,Kwangju,35.123173,126.805444
Spain,FUE,Fuerteventura Airport,Fuerteventura,28.452700,-13.863800
Sweden,\\N,Malmen Air Base,Linkoeping,58.402302,15.525700
Switzerland,\\N,Les Eplatures Airport,Les Eplatures,47.083900,6.792840
Taiwan,KNH,Kinmen Airport,Kinmen,24.427900,118.359001
Thailand,DMK,Don Mueang International Airport,Bangkok,13.912600,100.607002
Turkey,\\N,Güvercinlik Airport,Ankara,39.935001,32.740799
Ukraine,KBP,Boryspil International Airport,Kiev,50.345001,30.894699
United Arab Emirates,AUH,Abu Dhabi International Airport,Abu Dhabi,24.433001,54.651100
United Kingdom,BFS,Belfast International Airport,Belfast,54.657501,-6.215830
United States,BTI,Barter Island LRRS Airport,Barter Island,70.134003,-143.582001
Venezuela,AGV,Oswaldo Guevara Mujica Airport,Acarigua,9.553375,-69.237869
Vietnam,DAD,Da Nang International Airport,Danang,16.043900,108.198997
"""

# Read the data into a pandas DataFrame
data_io = StringIO(data)
df = pd.read_csv(data_io)

contries_cities = defaultdict(dict)
for idx, row in df.iterrows():
    contries_cities[row["Country"]][row["City"]] = (row["Latitude"], row["Longitude"])
    