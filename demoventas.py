import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el archivo de datos
try:
    df = pd.read_excel("SalidaFinalVentas.xlsx")

    # Filtros
    region_filter = st.selectbox("Selecciona una Región", df['Region'].unique())
    state_filter = st.selectbox("Selecciona un Estado", df['State'].unique())

    # Aplicar filtros
    filtered_df = df[(df['Region'] == region_filter) & (df['State'] == state_filter)]

    # Mostrar el DataFrame filtrado
    st.dataframe(filtered_df)

    # Gráfica de pastel
    fig = px.pie(filtered_df, names='Category', title='Distribución por Categoría')
    st.plotly_chart(fig)

except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinal.xlsx' no se encuentra.")

except KeyError as e:
    st.error(f"Error: La columna '{e}' no se encuentra en el archivo. Asegúrate de que el archivo contenga las columnas correctas.")

except Exception as e:
    st.error(f"Error al leer el archivo o generar la gráfica: {e}")