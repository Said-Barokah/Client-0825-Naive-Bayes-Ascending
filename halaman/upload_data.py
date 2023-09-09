import streamlit as st
import pandas as pd
import time
import os
def app():
    st.title('APLIKASI KLASIFIKASI NAIVE BAYES')
    if (os.path.exists("data/data_master.csv")):
         st.text('Data master')
         df = pd.read_csv('data/data_master.csv')
         st.write(df)
    if (os.path.exists("data/meta/feature_data.csv")):
         st.text('Fitur yang digunakan dalam klasifikasi')
         feature = pd.read_csv('data/meta/feature_data.csv')
         st.write(list(feature['column']))
    if(os.path.exists("data/meta/feature_data.csv")):
        label = pd.read_csv('data/meta/label_data.csv')
        st.write('Fitur yang menjadi label yaitu',str(label['label'][0]))
    
    data = st.file_uploader("upload data berformat csv (untuk mengubah data master)", type=['csv'])
    if data is not None:
            dataframe = pd.read_csv(data)
            dataframe.columns = dataframe.columns.str.replace(' ', '')
            st.write(dataframe)
            col1, col2 = st.columns(2)
            with col1 :
                column = st.multiselect('Pilih kolom yang akan di digunakan, kecuali kolom label',
                list(dataframe.columns),
                )
            with col2 :
                label = st.selectbox("Pilih Kolom yang akan dijadikan label atau class :",
                list(dataframe.columns))
  
            label = pd.DataFrame(data={'label': [label]})
            feature_names = pd.DataFrame(data={'column' : column})
            if st.button('simpan data') :
                label.to_csv('data/meta/label_data.csv',index=False)
                feature_names.to_csv('data/meta/feature_data.csv',index=False)
                if os.path.exists("data/data_branch.csv"):
                    os.remove("data/data_branch.csv")
                
                dataframe.to_csv('data/data_master.csv',index=False)
                with st.spinner('tunggu sebentar ...'):
                    time.sleep(1)
                st.success('data berhasil disimpan')
                st.info('silakan beralih ke proses selanjutnya')
