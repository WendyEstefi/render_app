import pandas as pd
import scipy.stats
import streamlit as st
import time
import random

# variables de estado que se conservan entre ejecuciones
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])

st.title("Simulación de Lanzamiento de Moneda")
st.write("Haz clic en el botón para lanzar una moneda y ver el resultado.")

# Gráfico inicial
chart = st.line_chart([0.5])

# Función para simular lanzamientos con gráficos
def toss_coin_graph(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# Funcionalidad para lanzar una moneda simple
if st.button("Lanzar moneda"):
    resultado = random.choice(["Cara", "Cruz"])
    st.write(f"**Resultado:** {resultado}")

# Funcionalidad para lanzar varias veces
num_lanzamientos = st.number_input("Número de lanzamientos", min_value=1, max_value=100, value=1)

if st.button("Lanzar varias veces"):
    resultados = [random.choice(["Cara", "Cruz"]) for _ in range(num_lanzamientos)]
    st.write("**Resultados:**", resultados)

# Interfaz de usuario para lanzar una moneda con gráficos y estadísticas
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin_graph(number_of_trials)
    st.session_state['df_experiment_results'] = pd.concat([ 
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean]], 
                     columns=['no', 'iterations', 'mean'])
    ], axis=0)
    st.session_state['df_experiment_results'] = st.session_state['df_experiment_results'].reset_index(drop=True)

st.write(st.session_state['df_experiment_results'])
