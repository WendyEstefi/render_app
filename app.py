<<<<<<< HEAD
import pandas as pd
import scipy.stats
import streamlit as st
import time

# variables de estado que se conservan entre ejecuciones
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])

st.header('Lanzar una moneda')

# gráfico inicial
chart = st.line_chart([0.5])

# función para simular lanzamientos
def toss_coin(n):
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

# interfaz de usuario
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

# cuando se presiona el botón
if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean]],
                     columns=['no', 'iterations', 'mean'])
    ],
        axis=0)
    st.session_state['df_experiment_results'] = st.session_state['df_experiment_results'].reset_index(drop=True)

st.write(st.session_state['df_experiment_results'])


=======
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
>>>>>>> ec15b9ca48fd9f17e28b06a62f567edead71f324
