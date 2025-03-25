# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
@st.cache_data
def load_data():
    df = pd.read_excel("SalidaFinalVentas.xlsx", sheet_name="Datos")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Año"] = df["Order Date"].dt.year
    return df

df = load_data()

st.title("📊 Dashboard de Ventas")

# Filtros
years = df["Año"].unique()
segmentos = df["Segment"].unique()

año_seleccionado = st.selectbox("Selecciona un año", sorted(years))
segmento_seleccionado = st.selectbox("Selecciona un segmento", sorted(segmentos))

df_filtrado = df[(df["Año"] == año_seleccionado) & (df["Segment"] == segmento_seleccionado)]

# Gráfico de barras: Ventas por región
st.subheader("Ventas por Región")
ventas_region = df_filtrado.groupby("Region")["Sales"].sum()
st.bar_chart(ventas_region)

# Gráfico de pastel: Ventas por Segmento
st.subheader("Distribución de Ventas por Segmento (año completo)")
ventas_segmento = df[df["Año"] == año_seleccionado].groupby("Segment")["Sales"].sum()
fig1, ax1 = plt.subplots()
ax1.pie(ventas_segmento, labels=ventas_segmento.index, autopct="%1.1f%%")
ax1.axis("equal")
st.pyplot(fig1)

# Gráfico de línea: Ventas por fecha
st.subheader("Ventas a lo largo del tiempo")
ventas_tiempo = df_filtrado.groupby("Order Date")["Sales"].sum()
st.line_chart(ventas_tiempo)

# Mostrar tabla
st.subheader("Datos filtrados")
st.dataframe(df_filtrado)