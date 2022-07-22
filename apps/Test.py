from apps.__packages import load_data, lottie
import streamlit as st
import numpy as np


def app(): 
    
    data = load_data.load_data()

    st.write("data_num : ", len(data['primaryid']))
    st.write("OK DataLoad")    


    st.write("age sum ",len(data["age_yr"][:]) ,np.sum(data["age_yr"][:]))

    