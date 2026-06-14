import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ckd_model.pkl")

st.title("Chronic Kidney Disease Prediction")

age = st.number_input("Age", min_value=1, max_value=100, value=30)

bp = st.number_input("Blood Pressure (mm/Hg)", min_value=50, max_value=200, value=120)

creatinine = st.number_input("Serum Creatinine (mg/dl)", min_value=0.1, max_value=20.0, value=1.0)

urea = st.number_input("Blood Urea (mg/dl)", min_value=1, max_value=400, value=25)

egfr = st.number_input("eGFR", min_value=1, max_value=150, value=90)

if st.button("Predict"):

    input_data = pd.DataFrame([[
        age,
        bp,
        creatinine,
        urea,
        egfr
    ]], columns=[
        'Age of the patient',
        'Blood pressure (mm/Hg)',
        'Serum creatinine (mg/dl)',
        'Blood urea (mg/dl)',
        'Estimated Glomerular Filtration Rate (eGFR)'
    ])

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("No CKD Detected")
    else:
        st.error("CKD Detected")
