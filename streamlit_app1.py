import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard COVID-19 Colombia")

df = pd.read_csv("Fallecidos_COVID_Colombia.csv")
df['Fecha de muerte'] = pd.to_datetime(df['Fecha de muerte'], errors='coerce')
df = df.dropna(subset=['Fecha de muerte'])
df['ID'] = 1

st.subheader("Fallecimientos semanales")
weekly = df.set_index('Fecha de muerte').resample('W')['ID'].sum()
st.line_chart(weekly)

st.subheader("Fallecidos por sexo")
st.bar_chart(df['Sexo'].value_counts())

st.subheader("Distribución de edades")
st.hist(df['Edad'].dropna(), bins=30)
