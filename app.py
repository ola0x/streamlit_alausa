import streamlit as st
import alausa, magodo, olaketu, giyan, majidun, ijede, ojokoro, maya, isiwu, imota

# st.title("The site is under Upgrade...")

st.title('Weather Report Dashboard')

st.markdown("The dashboard will visualize the correlation between The Constructed Instrument weather data and Standard Instrument Weather data")

# Sidebar Navigation
st.sidebar.write('# Location')
options = st.sidebar.radio('Select across 10 locations:', 
    ['ALAUSA', 'MAGODO ISHERI', 'MAJIDUN WETLAND', 'OJOKORO IKORODU', 'OLAKETU IKORODU', 'MAYA', 'ISIWU', 'IMOTA IKORODU', 'ODOGIYAN IKORODU', 'IJEDE'])

if options == 'ALAUSA':
    alausa.home()
elif options == 'MAGODO ISHERI':
    magodo.home()
elif options == 'MAJIDUN WETLAND':
    majidun.home()
elif options == 'OJOKORO IKORODU':
    ojokoro.home()
elif options == 'OLAKETU IKORODU':
    olaketu.home()
elif options == 'MAYA':
    maya.home()
elif options == 'ISIWU':
    isiwu.home()
elif options == 'IMOTA IKORODU':
    imota.home()
elif options == 'ODOGIYAN IKORODU':
    giyan.home()
elif options == 'IJEDE':
    ijede.home()