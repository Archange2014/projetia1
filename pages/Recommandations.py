import streamlit as st
import pandas as pd
# Chargement du dataset
data = pd.read_csv('BeansDataSet.csv')  #

st.subheader("Recommandations")
st.markdown("""
    - **Renforcez les ventes Arabica avec des campagnes dans la région Sud.**
    - **Ciblez les clients en ligne pour Espresso et Cappuccino.**
    - **Lancez des promotions saisonnières pour le Latté.**
    """)

