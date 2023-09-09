import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split

def app() :
    st.subheader('Split Data menjadi Data Training dan Data Testing')
    data = pd.read_csv('data/main_data.csv')
    test_size = (st.number_input('Data test Sebanyak',min_value=0.0,max_value=1.0,value=0.2,step=0.1,key='test_size'))
    X_train, X_test = train_test_split(data, test_size=test_size, random_state=1221)
    st.write(f'Data Train berjumlah {X_train.shape[0]}')
    st.write(X_train)
    st.write(f'Data Test berjumlah {X_test.shape[0]}')
    st.write(X_test)
    df_test_size = pd.DataFrame(data={ 'test size': [test_size]})
    df_test_size.to_csv('data/meta/test_size.csv',index=False)
