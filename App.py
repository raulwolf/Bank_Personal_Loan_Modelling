import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title('Thera Bank MVM')

model_load_state = st.text('Loading Model...')

model_path = './4_Model/decission_tree.sav'
loaded_model = pickle.load(open(model_path, 'rb'))

model_load_state.text("Model Loaded")

st.subheader('Datos del cliente')

agebin_31_40         = st.toggle('Edad entre 31-40', value = False)
agebin_41_50         = st.toggle('Edad entre 41-50', value = False)
agebin_51_60         = st.toggle('Edad entre 51-60', value = False)
agebin_60_100        = st.toggle('Edad entre 60-100', value = False)
income_group_medio   = st.toggle('Ingreso medio', value = False)
income_group_alto    = st.toggle('Ingreso alto', value = False)
spending_group_medio = st.toggle('Gasto medio', value = False)
spending_group_alto  = st.toggle('Gasto alto', value = False)


input_data = [
    [
        agebin_31_40, agebin_41_50, agebin_51_60, agebin_60_100, 
        income_group_medio, income_group_alto, 
        spending_group_medio, spending_group_alto
    ]
]

st.subheader('Resultado del modelo')

prediction = loaded_model.predict(input_data)[0]

if prediction == 0:
    st.text('El cliento NO aceptara un prestamo')
if prediction == 1:
    st.text('El cliento SI aceptara un prestamo')

