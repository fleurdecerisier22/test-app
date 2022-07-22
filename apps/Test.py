from apps.__packages import load_data, lottie
import streamlit as st


import time


def app(): 
    
    data, name2id, id2name, pt_name2socname = load_data.load_data()
    st.write(data['area'][-1])
    
    with lottie.get_lottie():
        time.sleep(10)

    