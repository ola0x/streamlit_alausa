import streamlit as st
import alausa
import magodo

# st.title("The site is under Upgrade...")

st.title('Weather Report Dashboard')

st.markdown("The dashboard will visualize the correlation between The Constructed Instrument weather data and Standard Instrument Weather data")

# Sidebar Navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select across 10 locations:', 
    ['ALAUSA', 'MAGODO', 'MAJIDUN', 'OJOKORO IKORODU', 'OLAKETU IKORODU', 'MAYA', 'ISIWU', 'IMOTA IKORODU', 'ODOGIYAN IKORODU', 'IJEDE'])

if options == 'ALAUSA':
    alausa.home()
elif options == 'MAGODO':
    magodo.home()
elif options == 'MAJIDUN':
    raw_data.raw_data(las_file, well_data)
elif options == 'OJOKORO IKORODU':
    plotting.plot(las_file, well_data)
elif options == 'OLAKETU IKORODU':
    home.home()
elif options == 'MAYA':
    home.home()
elif options == 'ISIWU':
    home.home()
elif options == 'IMOTA IKORODU':
    home.home()
elif options == 'ODOGIYAN IKORODU':
    home.home()
elif options == 'IJEDE':
    home.home()