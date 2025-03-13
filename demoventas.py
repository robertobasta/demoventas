import streamlit as st
import pandas as pd
import plotly.express as px

# Sample DataFrame (replace with your actual data)
data = {'Region': ['Norte', 'Norte', 'Norte', 'Sur', 'Sur', 'Sur', 'Este', 'Este', 'Este', 'Oeste', 'Oeste', 'Oeste'],
        'Estado': ['Aguascalientes', 'Coahuila', 'Chihuahua', 'Michoacán', 'Guerrero', 'Oaxaca', 'Veracruz', 'Tabasco', 'Quintana Roo', 'Baja California', 'Sonora', 'Sinaloa'],
        'Categoria': ['Electronica', 'Ropa', 'Hogar', 'Electronica', 'Ropa', 'Hogar', 'Electronica', 'Ropa', 'Hogar','Electronica', 'Ropa', 'Hogar'],
        'Valor': [10, 15, 12, 8, 11, 16, 13, 9, 7, 14, 10, 6]}
df = pd.DataFrame(data)

st.title("Gráfico de Pastel de Categorías por Región y Estado")

# Region filter
selected_region = st.selectbox("Selecciona una Región", df['Region'].unique())

# Filter the DataFrame based on the selected region
filtered_df = df[df['Region'] == selected_region]

# State filter
selected_state = st.selectbox("Selecciona un Estado", filtered_df['Estado'].unique())

# Filter the DataFrame based on the selected state
filtered_df = filtered_df[filtered_df['Estado'] == selected_state]


# Create the pie chart
fig = px.pie(filtered_df, names='Categoria', values='Valor', title=f"Categorías de Productos en {selected_state}, {selected_region}")
st.plotly_chart(fig)
