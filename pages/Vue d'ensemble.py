import streamlit as st
import pandas as pd

# Chargement du dataset
data = pd.read_csv('BeansDataSet.csv')  #


st.subheader("Statistiques globales")
st.write(data.describe())
    
st.subheader("Ventes par canal")
channel_sales = data.groupby("Channel").sum()
st.bar_chart(channel_sales)
