import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
# Chargement du dataset
data = pd.read_csv('BeansDataSet.csv')  

st.subheader("Ventes par région")
region_sales = data.groupby("Region")[["Robusta", "Arabica", "Espresso", "Lungo", "Latte", "Cappuccino"]].sum()
st.bar_chart(region_sales)

st.subheader("Corrélations entre produits")
fig, ax = plt.subplots()
ax.matshow(data.corr(), cmap="coolwarm")
st.pyplot(fig)