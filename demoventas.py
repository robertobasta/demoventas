import streamlit as st
import pandas as pd
import plotly.express as px

# Load the Excel file
try:
    df = pd.read_excel("/workspaces/demoventas/SalidaFinalVentas.xlsx")
except FileNotFoundError:
    st.error("El archivo 'SalidaFinalVentas.xlsx' no se encontró. Por favor, asegúrate de que el archivo esté en el directorio '/workspaces/demoventas/'.")
    st.stop()

# Mostrar el DataFrame
st.write(df)

st.title("Gráfico de Pastel de Categorías de Productos")

# Region filter
available_regions = df['Region'].unique()
selected_region = st.selectbox("Selecciona una región:", available_regions)

# Filter data based on the selected region
filtered_df = df[df['Region'] == selected_region]

# Year filter
available_years = df['Año'].unique()
selected_year = st.selectbox("Selecciona un año:", available_years)

# Filter data based on the selected year
filtered_df = filtered_df[filtered_df['Año'] == selected_year]

# Check if 'Estado' column exists in the original dataframe
if 'Estado' in df.columns:
    # Check if 'Estado' column exists in the filtered dataframe
    if 'Estado' in filtered_df.columns:
        # State filter (dependent on the selected region)
        available_states = filtered_df['Estado'].unique()
        selected_state = st.selectbox("Selecciona un estado:", available_states)

        # Filter data based on the selected state
        filtered_df = filtered_df[filtered_df['Estado'] == selected_state]

        # Create the pie chart
        if not filtered_df.empty:
            fig = px.pie(filtered_df, names='CategoriaProducto', title=f"Categorías de Productos en {selected_state}, {selected_region} en {selected_year}", hole=0.3)
            st.plotly_chart(fig)
        else:
            st.warning("No hay datos disponibles para la región, estado y año seleccionados.")
    else:
        st.error("La columna 'Estado' no se encuentra en los datos filtrados. Por favor, verifica el archivo Excel.")
else:
    st.error("La columna 'Estado' no se encuentra en los datos. Por favor, verifica el archivo Excel.")

# Crear el gráfico de barras
st.title("Gráfico de Barras de Ventas por Categoría de Producto")

# Filtrar los datos para el gráfico de barras
bar_chart_df = filtered_df.groupby('CategoriaProducto')['Ventas'].sum().reset_index()

# Crear el gráfico de barras
fig_bar = px.bar(bar_chart_df, x='CategoriaProducto', y='Ventas', title=f"Ventas por Categoría de Producto en {selected_region} en {selected_year}")

# Mostrar el gráfico de barras
st.plotly_chart(fig_bar)