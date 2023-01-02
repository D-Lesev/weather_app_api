import streamlit as st
import plotly.express as px
from backend import get_data


st.title('Weather Forcast for next days')
place = st.text_input('Place: ')
days = st.slider("Forcast for next days", min_value=1, max_value=5, help="Select the number of forecast days")

options = st.selectbox("Select data to be represent",
                       ("Temperature", "Sky"))

st.subheader(f"{options} for the next {days} in {place}")

if place:

    filtered_data = get_data(place, days)

    if options == "Temperature":
        temps = [dict["main"]["temp"] / 10 for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]

        figure = px.line(x=dates, y=temps, labels={"x": "Date",  "y": "Temperature (C)"})
        st.plotly_chart(figure)

    else:
        sky_cond = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {
            "Clear": "images/clear.png",
            "Clouds": "images/cloud.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png"
        }

        filtered_images = [images[sky] for sky in sky_cond]

        st.image(filtered_images, width=115)
