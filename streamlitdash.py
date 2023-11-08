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
    df = pd.read_csv(filename, encoding="ISO-8859-1")
else:
    os.chdir(r"C:\Users\bradd\Documents\DATA SCIENCE\PROJECTS\streamlitdashboard")
    df = pd.read_csv("SampleSuperstore.csv", encoding="ISO-8859-1")
col1, col2 = st.columns((2))
df['Order Date'] = pd.to_datetime(df['Order Date'], format="mixed")

# Getting min and max date
startDate = pd.to_datetime(df['Order Date']).min()
endDate = pd.to_datetime(df['Order Date']).max()

with col1:
    date1 = pd.to_datetime(st.date_input("Order Date", startDate))

with col2:
    date2 = pd.to_datetime(st.date_input("Order Date", endDate))

df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

# Region Filter
st.sidebar.header("Choose Your Filter:")
region = st.sidebar.multiselect("Pick the Region", df["Region"].unique())

if not region:
    df2 = df.copy()
else:
    df2 = df[df["Region"].isin(region)]

# State Filter
state = st.sidebar.multiselect("Pick the State", df2["State"].unique())
if not state:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(state)]

# City Filter
city = st.sidebar.multiselect("Pick the City", df3["City"].unique())

# Filter the data based on Region, State and City
if not region and not state and not city:
    filtered_df = df
elif not state and not city:
    filtered_df = df[df["Region"].isin(region)]
elif not region and not city:
    filtered_df = df[df["State"].isin(state)]
elif state and city:
    filtered_df = df3[df["State"].isin(state) & df3["City"].isin(city)]
elif region and city:
    filtered_df = df3[df["State"].isin(region) & df3["City"].isin(city)]
elif state and city:
    filtered_df = df3[df["State"].isin(region) & df3["City"].isin(state)]
elif city:
    filtered_df = df3[df3["City"].isin(city)]
else:
    filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df3["City"].isin(city)]