import streamlit as st
import requests

API_KEY="c555d51a2de0407ba27150017250512"

st.title("My Weather Dashboard")
st.write("Welcome to my weather dashboard application!")

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=1&aqi=no&alerts=no"
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.ConnectionError:
         return None

city = st.text_input("Enter city name:", "Cairo")
if st.button("Submit"):
    data=get_weather(city)
    if data is None:
        st.write("Error fetching data. Please check your connection.")
    else:
            name= data['location']['name']
            country=data['location']['country']
            main = data['current']['condition']['text']
            temp = data["current"]["temp_c"]
            feels = data["current"]["feelslike_c"]
            humidity = data["current"]["humidity"]
            wind = data["current"]["wind_mph"]
            visibility = data['current']['vis_km']
            icon_url = "https:"+data["current"]["condition"]["icon"]
            st.subheader(f"Weather in {name}, {country}")
            st.image(icon_url)
            st.write('Weather Condition:', main)
            st.divider(width='stretch')
            col1,col2,col3, col4= st.columns(4)  
            col1.metric(label="Temperature (°C)", value=f"{temp} °C", delta=f"Feels like {feels} °C",border=True)
            col2.metric(label="Humidity (%)", value=f"{humidity} %",border=True)
            col3.metric(label="Wind Speed (m/s)", value=f"{wind} m/s",border=True)
            col4.metric(label="Visibility (km)", value=f"{visibility} km",border=True)
