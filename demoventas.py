import pandas as pd
import streamlit as st
import subprocess
import sys

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    st.error("Error: matplotlib no está instalado. Instalando matplotlib...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt

# Conectar con el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')
except FileNotFoundError:
    st.error("Error: El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
    st.stop()

# Crear gráficos con la información
def crear_graficos():
    st.title('Sales Analysis')

    # Verificar que las columnas necesarias existen en el DataFrame
    required_columns = ['Product', 'Sales']
    for col in required_columns:
        if col not in df.columns:
            st.error(f"Error: La columna '{col}' no existe en el archivo Excel.")
            st.stop()

    # Gráfico de barras de ventas por producto
    if 'Product' in df.columns and 'Sales' in df.columns:
        st.subheader('Sales by Product')
        fig, ax = plt.subplots()
        df.groupby('Product')['Sales'].sum().plot(kind='bar', ax=ax)
        ax.set_title('Sales by Product')
        ax.set_xlabel('Product')
        ax.set_ylabel('Sales')
        st.pyplot(fig)

# Llamar a la función para crear los gráficos
if __name__ == '__main__':
    crear_graficos()

