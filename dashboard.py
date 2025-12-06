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
            hours = data["forecast"]["forecastday"][0]["hour"]

            st.markdown("""
            <style>
            .hour-scroll {
                display: flex;  /*Aligns items in a row */
                overflow-x: scroll; /*Allows horizontal scrolling if content overflows */
                gap: 15px;
                padding: 10px;
            }
            .hour-card {
                min-width: 100px; /* sets maximum width of each card */
                padding: 10px;
                background: #1e1e1e;
                color: white;
                border-radius: 10px;
                text-align: center;
            }
            .hour-card img {
                width: 40px;
            }
            </style>
            """, unsafe_allow_html=True)
            html = '<div class="hour-scroll">'
            for h in hours:
                hour_label = h["time"].split(" ")[1]      # only HH:MM
                temp_c = h["temp_c"]
                icon = "https:" + h["condition"]["icon"]

                html += f'<div class="hour-card">'
                html += f'<p>{hour_label}</p>'
                html += f'<img src="{icon}">'
                html += f'<p>{temp_c}°C</p>'
                html += '</div>'

            html += '</div>'

            st.markdown(html, unsafe_allow_html=True)

