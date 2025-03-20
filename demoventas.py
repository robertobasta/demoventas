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
    required_columns = ['Producto', 'Ventas']
    for col in required_columns:
        if col not in df.columns:
            st.error(f"Error: La columna '{col}' no existe en el archivo Excel.")
            st.stop()

    # Gráfico de barras de ventas por producto
    if 'Producto' in df.columns and 'Ventas' in df.columns:
        st.subheader('Ventas por Producto')
        fig, ax = plt.subplots()
        df.groupby('Producto')['Ventas'].sum().plot(kind='bar', ax=ax)
        ax.set_title('Ventas por Producto')
        ax.set_xlabel('Producto')
        ax.set_ylabel('Ventas')
        st.pyplot(fig)

# Llamar a la función para crear los gráficos
if __name__ == '__main__':
    crear_graficos()

