import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import random

def generate_dummy_weather(month, year, location=None):
    days_in_month = (datetime(year, month + 1, 1) - timedelta(days=1)).day
    weather_code_data = {day: random.choice([1,2,3]) for day in range(1, days_in_month + 1)}
    return weather_code_data

def create_calendar_view(weather_data, month, year):
    data = []
    for day, weather in weather_data.items():
        data.append({'Date': datetime(year, month, day), 'Weather': weather})
    df = pd.DataFrame(data)
    df.set_index('Date', inplace=True)
    st.write(df)

weather_code_to_icons = {1:'☀️', 2:'☁️', 3:'🌧️'}
# Main Streamlit app
st.title("Travel Planner")

# Input for selecting month
selected_month = st.selectbox("Select Month", range(1, 13))
detailed_month = st.checkbox("Detailed Month Selection")

if detailed_month:
    start_date = st.date_input("Start Date", datetime.today())
    end_date = st.date_input("End Date", datetime.today() + timedelta(days=1))

# Input for selecting region
regions = {
    "France": ["Paris", "Nice", "Lyon"],
    "USA": ["New York", "Los Angeles", "Chicago"],
    "Japan": ["Tokyo", "Osaka", "Kyoto"]
}

selected_region = st.selectbox("Select Region", regions.keys())
detailed_region = st.checkbox("Detailed Region Selection")

if detailed_region:
    selected_city = st.selectbox("Select City", regions[selected_region])
    address = st.text_input("Enter Detailed Address")

# Generate dummy weather data for the selected month
year = datetime.now().year
weather_data = generate_dummy_weather(selected_month, year)
weather_data = {j:weather_code_to_icons[i] for j, i in weather_data.items()}

# Show calendar view with weather data
if st.button("Show Weather Calendar"):
    st.header(f"Weather Calendar for {selected_month}/{year}")
    create_calendar_view(weather_data, selected_month, year)
