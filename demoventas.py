import streamlit as st
import pandas as pd
import plotly.express as px

# Load the Excel file
try:
    df = pd.read_excel("SalidaFinalVentas.xlsx")
except FileNotFoundError:
    st.error("El archivo 'SalidaFinalVentas.xlsx' no se encontró. Por favor, asegúrate de que el archivo esté en el mismo directorio que la aplicación Streamlit.")
    st.stop()


st.title("Gráfico de Pastel de Categorías de Productos")

# Region filter
available_regions = df['Region'].unique()
selected_region = st.selectbox("Selecciona una región:", available_regions)


# Filter data based on the selected region
filtered_df = df[df['Region'] == selected_region]

# State filter (dependent on the selected region)
available_states = filtered_df['Estado'].unique()
selected_state = st.selectbox("Selecciona un estado:", available_states)


# Filter data based on the selected state
filtered_df = filtered_df[filtered_df['Estado'] == selected_state]


# Create the pie chart
if not filtered_df.empty:
    fig = px.pie(filtered_df, names='CategoriaProducto', title=f"Categorías de Productos en {selected_state}, {selected_region}", hole=0.3)
    st.plotly_chart(fig)
else:
    st.warning("No hay datos disponibles para la región y estado seleccionados.")
