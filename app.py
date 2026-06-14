import streamlit as st

st.title("Chronic Kidney Disease Prediction")

age = st.number_input("Age")

bp = st.number_input("Blood Pressure")

creatinine = st.number_input("Serum Creatinine")

urea = st.number_input("Blood Urea")

egfr = st.number_input("eGFR")

if st.button("Predict"):

    if creatinine > 1.5 or urea > 50 or egfr < 60:
        st.error("CKD Risk Detected")
    else:
        st.success("No CKD Risk Detected")
