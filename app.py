import streamlit as st
import pandas as pd

st.title("Weather Report Dashboard For Alausa")

st.markdown("The dashboard will visualize the correlation between The Constructed Instrument weather data and Standard Instrument Weather data")

def load_data():
    data=pd.read_excel("data.xlsx")
    return data

data=load_data()

#st.write(covid_data)
st.table(data)

db_data = data[['SS', 'CS']]
temp_data = data[['ST', 'CT']]
rh_data = data[['SRH', 'CRH']]
pbar_data = data[['SP', 'CP']]

st.write("S [db] data for both the Constructed and Standard Instrument")
st.line_chart(db_data)
st.write("Temperature data for both the Constructed and Standard Instrument")
st.line_chart(temp_data)
st.write("RH [%] data for both the Constructed and Standard Instrument")
st.line_chart(rh_data)
st.write(" P [mbar] data for both the Constructed and Standard Instrument")
st.line_chart(pbar_data)