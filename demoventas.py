import streamlit as st
import pandas as pd
import plotly.express as px

# Sample DataFrame (replace with your actual data)
data = {'Zona': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte', 'Sur', 'Este', 'Oeste'],
        'Valor': [10, 15, 12, 8, 11, 16, 13, 9]}
df = pd.DataFrame(data)

st.title("Gráfico por Zona")

# Select the column for the chart's y-axis
y_column = st.selectbox("Selecciona la columna para el eje Y:", df.columns)

# Create the chart based on the selected column and zone
if y_column:
    fig = px.bar(df, x="Zona", y=y_column, title=f"Gráfico de {y_column} por Zona", color='Zona')
    st.plotly_chart(fig)
else:
    st.warning("Por favor, selecciona una columna para el eje Y.")
