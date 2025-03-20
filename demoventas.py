import pandas as pd
import streamlit as st

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    st.error("Error: matplotlib no está instalado. Por favor, instálalo para continuar.")

# Conectar con el archivo Excel
df = pd.read_excel('SalidaFinalVentas.xlsx')

# Crear gráficos con la información
def crear_graficos():
    st.title('Análisis de Ventas')

    # Gráfico de barras de ventas por producto
    st.subheader('Ventas por Producto')
    fig, ax = plt.subplots()
    df.groupby('Producto')['Ventas'].sum().plot(kind='bar', ax=ax)
    ax.set_title('Ventas por Producto')
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas')
    st.pyplot(fig)

    # Gráfico de líneas de ventas por mes
    st.subheader('Ventas por Mes')
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    df.set_index('Fecha', inplace=True)
    fig, ax = plt.subplots()
    df.resample('M')['Ventas'].sum().plot(kind='line', ax=ax)
    ax.set_title('Ventas por Mes')
    ax.set_xlabel('Mes')
    ax.set_ylabel('Ventas')
    st.pyplot(fig)

# Llamar a la función para crear los gráficos
if __name__ == '__main__':
    crear_graficos()