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

# for idx, row in iata_codes.iterrows():
#     CODES[row["IATA"]] = (row["Latitude"], row["Longitude"], row["Country"], row["City"])
