import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_excel("SalidaFinalVentas.xlsx", sheet_name="Datos")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Año"] = df["Order Date"].dt.year
    return df

df = load_data()

st.title("📈 Dashboard de Ventas Superstore")

# Gráfica 1: Ventas por Año, Categoría y Sub-Categoría (facet_col=Category)
st.subheader("Gráfica 1: Ventas por Año, Categoría y Sub-Categoría")
fig1 = px.bar(
    df,
    x="Año",
    y="Sales",
    color="Sub-Category",
    facet_col="Category",
    title="Ventas Acumuladas por Año, Categoría y Sub-Categoría",
    labels={"Sales": "Ventas"},
    height=500
)
st.plotly_chart(fig1)

# Gráfica 2: Ventas por Año, Categoría y Sub-Categoría (facet_col=Año)
st.subheader("Gráfica 2: Ventas por Año, Categoría y Sub-Categoría (Distribuidas por Año)")
fig2 = px.bar(
    df,
    x="Category",
    y="Sales",
    color="Sub-Category",
    facet_col="Año",
    title="Ventas por Categoría y Sub-Categoría en cada Año",
    labels={"Sales": "Ventas"},
    height=500
)
st.plotly_chart(fig2)

# Gráfica 3: Línea de ventas acumuladas por año y categoría
st.subheader("Gráfica 3: Línea de Ventas por Año y Categoría")
df_line = df.groupby(["Año", "Category"])["Sales"].sum().reset_index()
fig3 = px.line(
    df_line,
    x="Año",
    y="Sales",
    color="Category",
    title="Ventas Acumuladas por Año y Categoría",
    labels={"Sales": "Ventas"},
    markers=True
)
st.plotly_chart(fig3)

# Gráfica 4: Barras de ventas acumuladas por región
st.subheader("Gráfica 4: Ventas Acumuladas por Región")
df_region = df.groupby("Region")["Sales"].sum().reset_index()
fig4 = px.bar(
    df_region,
    x="Region",
    y="Sales",
    title="Ventas Acumuladas por Región",
    labels={"Sales": "Ventas"},
    height=400
)
st.plotly_chart(fig4)