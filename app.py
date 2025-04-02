import streamlit as st
import random

st.title("Simulación de Lanzamiento de Moneda")

st.write("Haz clic en el botón para lanzar una moneda y ver el resultado.")

if st.button("Lanzar moneda"):
    resultado = random.choice(["Cara", "Cruz"])
    st.write(f"**Resultado:** {resultado}")

num_lanzamientos = st.number_input("Número de lanzamientos", min_value=1, max_value=100, value=1)

if st.button("Lanzar varias veces"):
    resultados = [random.choice(["Cara", "Cruz"]) for _ in range(num_lanzamientos)]
    st.write("**Resultados:**", resultados)
