import streamlit as st
import pandas as pd
from halaman import upload_data,pre_processing, data_split, classification
page_names_to_funcs = {
    "Upload Data" : upload_data.app,
    "Pre Processing" : pre_processing.app,
    "Data Split" : data_split.app,
    "Classification" : classification.app
}

demo_name = st.sidebar.selectbox("halaman", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()