import streamlit as st
import pandas as pd

def load_data():
    data=pd.read_excel("maya.xlsx")
    return data

def home():
    data=load_data()

    st.write('## Report for MAYA')
    st.table(data)

    db_data = data[['SS', 'CS']]
    temp_data = data[['ST', 'CT']]
    rh_data = data[['SRH', 'CRH']]
    pbar_data = data[['SP', 'CP']]

    max_ss, max_cs = db_data.max()
    min_ss, min_cs = db_data.min()
    max_st, max_ct = temp_data.max()
    # st.text(max_ss)
    # st.text(max_cs)
    # st.text(min_ss)
    # st.text(min_cs)

    st.write(" S [db] data for both the Constructed and Standard Instrument")
    st.line_chart(db_data)
    st.write("Temperature data for both the Constructed and Standard Instrument")
    st.line_chart(temp_data)
    st.write("RH [%] data for both the Constructed and Standard Instrument")
    st.line_chart(rh_data)
    st.write(" P [mbar] data for both the Constructed and Standard Instrument")
    st.line_chart(pbar_data)