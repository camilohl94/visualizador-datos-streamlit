import streamlit as st
import pandas as pd

st.title('Visor de datos de CSV')
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1', delimiter=';')
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
