import streamlit as st
import plotly.express as px
import data

st.title("Weather forecast")

place = st.text_input("Place: ")
days = st.slider("Forecast days", min_value=1, max_value=5)
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if option == "Temperature":
    temperatures, dates = data.get(place, days, option)
    figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature (C)"})
    st.plotly_chart(figure)
    