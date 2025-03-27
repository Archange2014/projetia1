import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Chargement du dataset
data = pd.read_csv('BeansDataSet.csv')  # Remplacez par le chemin correct

# Vérifiez les colonnes disponibles
st.title("Analyse des données Beans & Pods")
st.write("Aperçu des données :")
st.dataframe(data.head())

# Gestion des colonnes numériques
numeric_data = data.select_dtypes(include=['float', 'int']).dropna()

# Calcul de la matrice de corrélation
correlation_matrix = numeric_data.corr()

# Visualisation
fig, ax = plt.subplots()
cax = ax.matshow(correlation_matrix, cmap="coolwarm")
fig.colorbar(cax)
ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_yticks(range(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=90)
ax.set_yticklabels(correlation_matrix.columns)
st.pyplot(fig)