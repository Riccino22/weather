import streamlit as st
import plotly.express as px
import data

st.title("Weather forecast")

place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
        if option == "Temperature":
            unit = st.selectbox("Select a unit", ("Kelvin", "Celcius", "Fahrenheit"))
            temperatures, dates = data.get(place, days, option, unit)
            figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            sky_condition, dates = data.get(place, days, option)
            for index, sky in enumerate(sky_condition):
                st.subheader(sky["main"])
                st.write(sky["description"])
                st.write(dates[index])
except KeyError:
    st.error("Place not found")