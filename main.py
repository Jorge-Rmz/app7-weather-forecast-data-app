import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, subheader
st.title("Weather Forecast for the next days ")
place = st.text_input("Place: ")
days = st.slider("Forecast Days ", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"Temperature for the next {days} days in {place}")
try:
    if place:
        # Get the temperature data
        data_filtred = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict['main']['temp']/10 for dict in data_filtred]
            # temperatures = [(tem - 32) * 5/9 for tem in temperatures]
            dates = [dict['dt_txt'] for dict in data_filtred]
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y": "Temperature (C)" } )
            st.plotly_chart(figure)

        if option == "Sky":
            images ={"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                     "Rain": "images/rain.png", "Snow": "images/snow.png"}
            data_filtred = [dict['weather'][0]['main'] for dict in data_filtred]

            images_path = [images[condition] for condition in data_filtred]


            st.image(images_path, width=115 )
except KeyError:
    st.error("This place no exist, please enter a place existent")