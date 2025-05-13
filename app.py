import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np
import os

st.set_page_config(page_title="Portafolio de Sostenibilidad", layout="wide")
st.title("Portafolio de Reflexión: Sostenibilidad")

tab1, tab2, tab3 = st.tabs(["Lo que veo", "Lo que ignoro", "Lo que eligo"])

with tab1:
    st.header("Lo que veo")
    st.write("Escenas cotidianas que se han normalizado, pero que reflejan la insostenibilidad del sistema actual.")
    col1, col2 = st.columns(2)

    with col1:
        st.image("img/Lo_que_veo/gula2.jpg", caption="Acumulación de basura en espacios públicos", use_column_width=True)
    with col2:
        st.image("img/Lo_que_veo/supermercado.jpg", caption="Tráfico urbano constante", use_column_width=True)

# --- TAB 2: Lo que ignoro ---
with tab2:
    st.header("Lo que ignoro")
    st.write("Impactos ocultos en las cadenas de producción: explotación, residuos tóxicos y daño ambiental.")
    col1, col2 = st.columns(2)

    with col1:
        st.image("img/Lo_que_ignoro/fabrica.jpg", caption="Condiciones laborales en fábricas textiles", use_column_width=True)
    with col2:
        st.image("img/Lo_que_ignoro/images.jpg", caption="Desechos electrónicos acumulados", use_column_width=True)

# --- TAB 3: Lo que elijo ---
with tab3:
    st.header("Lo que elijo")
    st.write("Iniciativas que muestran que otro camino es posible: colaboración, regeneración y sostenibilidad.")
    col1, col2 = st.columns(2)

    with col1:
        st.image("img/Lo_que_elijo/caminar.jpg", caption="Huerta urbana comunitaria", use_column_width=True)
    with col2:
        st.image("img/Lo_que_elijo/econologia.jpg", caption="Movilidad sostenible en bicicleta", use_column_width=True)