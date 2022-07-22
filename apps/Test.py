from apps.__packages import load_data, lottie
import streamlit as st


import time


def app(): 
    
    data = load_data.load_data()

    st.write("data_num : ", len(data['primaryid']))
    st.write("OK DataLoad")    

    