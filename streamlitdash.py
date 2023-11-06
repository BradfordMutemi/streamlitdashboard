import numpy as np
import pandas as pd
import streamlit as st 
import plotly.express as px
import os

import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title='Superstore', page_icon=':bar_chart:', layout='wide')

st.title(":bar_chart: Superstore EDA")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
fl = st.file_uploader(":file_folder: Upload a file", type=(["csv", "txt", "xlsx", "xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df = pd.read_csv(filename)
else:
    os.chdir(r"C:\Users\bradd\Documents\DATA SCIENCE\PROJECTS\streamlitdashboard")
    df = pd.read_csv("SampleSuperstore.csv")

