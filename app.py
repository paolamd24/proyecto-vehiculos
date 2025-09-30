import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Vehículos", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")

df = load_data()


st.header("Análisis de vehículos en venta")


st.write(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
with st.expander("Vista previa del dataset"):
    st.dataframe(df.head())

st.divider()


st.subheader("Histograma de precios")
col_hist = st.selectbox("Selecciona la variable para el histograma", df.columns, index=0)
fig = px.histogram(df, x=col_hist, nbins=50, title=f"Distribución de {col_hist}")
st.plotly_chart(fig, use_container_width=True)

st.divider()


st.subheader("Precio vs Año del modelo")
fig2 = px.scatter(
    df,
    x="model_year",
    y="price",
    title="Precio de vehículos por año de modelo",
    opacity=0.5
)
st.plotly_chart(fig2, use_container_width=True)
