import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración general de la app
st.set_page_config(page_title="Dashboard COVID-19 Colombia", layout="wide")
st.title("📊 Dashboard de Fallecidos por COVID-19 en Colombia")

# Cargar datos
@st.cache_data
def cargar_datos():
    df = pd.read_csv("Fallecidos_COVID_Colombia_limpio.csv")
    df.columns = df.columns.str.strip()
    df['Fecha de muerte'] = pd.to_datetime(df['Fecha de muerte'], errors='coerce')
    df = df.dropna(subset=['Fecha de muerte', 'Edad', 'Sexo'])
    df['Edad'] = df['Edad'].astype(int)
    return df

df = cargar_datos()

# Fallecimientos semanales
st.subheader("📅 Fallecimientos semanales")
weekly = df.set_index('Fecha de muerte').resample('W')['ID de caso'].count()
st.line_chart(weekly)

# Fallecidos por sexo
st.subheader("⚧ Fallecidos por Sexo")
st.bar_chart(df['Sexo'].value_counts())

# Distribución de edades
st.subheader("🎂 Distribución de edades de los fallecidos")
fig, ax = plt.subplots(figsize=(10, 4))
df['Edad'].plot.hist(bins=30, ax=ax, color='orange', edgecolor='black')
ax.set_xlabel("Edad")
ax.set_ylabel("Cantidad de fallecidos")
ax.set_title("Histograma de edades")
st.pyplot(fig)

# Top 10 edades más frecuentes por sexo
st.subheader("🏆 Top 10 edades con más fallecidos por sexo")
top_edades = df.groupby(['Sexo', 'Edad']).size().reset_index(name='Fallecidos')
top_edades = top_edades.sort_values(by='Fallecidos', ascending=False).head(10)
st.dataframe(top_edades)
