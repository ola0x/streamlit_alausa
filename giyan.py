import streamlit as st
import pandas as pd

def load_data():
    data=pd.read_excel("giyan.xlsx")
    return data

def home():
    data=load_data()

    st.write('## Report for ODOGIYAN IKORODU')
    st.table(data)

    db_data = data[['SS', 'CS']]
    temp_data = data[['ST', 'CT']]
    rh_data = data[['SRH', 'CRH']]
    pbar_data = data[['SP', 'CP']]

    mean_ss, mean_cs = db_data.mean()
    mean_st, mean_ct = temp_data.mean()
    mean_srh, mean_crh = rh_data.mean()
    mean_sp, mean_cp = pbar_data.mean()
    errors = ((mean_ss - mean_cs) / (mean_cs)) * 100
    errort = ((mean_st - mean_ct) / (mean_ct)) * 100
    errorrh = ((mean_srh - mean_crh) / (mean_crh)) * 100
    errorp = ((mean_sp - mean_cp) / (mean_cp)) * 100
    # st.text(min_ss)
    # st.text(min_cs)

    st.write(" S [db] data for both the Constructed and Standard Instrument")
    errors = '{:,.2f}'.format(abs(errors))
    st.write('The Percentage error difference is ', errors, '%')
    st.line_chart(db_data)
    st.write("Temperature data for both the Constructed and Standard Instrument")
    errort = '{:,.2f}'.format(abs(errort))
    st.write('The Percentage error difference is ', errort, '%')
    st.line_chart(temp_data)
    st.write("RH [%] data for both the Constructed and Standard Instrument")
    errorrh = '{:,.2f}'.format(abs(errorrh))
    st.write('The Percentage error difference is ', errorrh, '%')
    st.line_chart(rh_data)
    st.write(" P [mbar] data for both the Constructed and Standard Instrument")
    errorp = '{:,.2f}'.format(abs(errorp))
    st.write('The Percentage error difference is ', errorp, '%')
    st.line_chart(pbar_data)