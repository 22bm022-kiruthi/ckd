import streamlit as st

st.title("Chronic Kidney Disease Prediction")

age = st.number_input("Age")

bp = st.number_input("Blood Pressure")

creatinine = st.number_input("Serum Creatinine")

if st.button("Predict"):
    st.success("Prediction Working")