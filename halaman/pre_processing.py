import streamlit as st
import pandas as pd
import time
import timeit

import swifter
def app():
    #Your statements here
    data = pd.read_csv('data/data_master.csv')
    data.columns = data.columns.str.replace(' ', '')
    data.to_csv('data/main_data.csv',index=False)

    st.sidebar.markdown("lakukan preprosesing data")
    st.subheader('Data sebelum di proses')
    st.write(data)
    with st.spinner('tunggu sebentar ...'):
        time.sleep(2)
        st.write(pd.DataFrame(data.isnull().sum(), columns=['missing value']))
        st.write(pd.DataFrame(data.loc[data.isnull().sum(axis=1) != 0].index, columns=['index ke-']))
        if(st.button('hapus data')):
            data = data.dropna()
            data.columns = data.columns.str.replace(' ', '')
            data.to_csv('data/main_data.csv',index=False)
            main_data = pd.read_csv('data/main_data.csv')
            st.subheader('Data setelah di proses')
            st.write(main_data)
                

