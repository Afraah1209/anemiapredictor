import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("anemia_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit app interface
st.title("Anemia Prediction App")
st.markdown("Enter the following blood test values to predict whether the person is anemic.")

# Input fields
age = st.number_input("Age", min_value=0.0, format="%.2f")
rbc = st.number_input("RBC (Red Blood Cell count)", min_value=0.0, format="%.2f")
pcv = st.number_input("PCV (Packed Cell Volume)", min_value=0.0, format="%.2f")
mcv = st.number_input("MCV (Mean Cell Volume)", min_value=0.0, format="%.2f")
mch = st.number_input("MCH (Mean Cell Hemoglobin)", min_value=0.0, format="%.2f")
mchc = st.number_input("MCHC (Mean Cell Hemoglobin Concentration)", min_value=0.0, format="%.2f")
rdw = st.number_input("RDW (Red Cell Distribution Width)", min_value=0.0, format="%.2f")
tlc = st.number_input("TLC (White Blood Cell count)", min_value=0.0, format="%.2f")
plt = st.number_input("Platelet Count (PLT /mm3)", min_value=0.0, format="%.2f")
hgb = st.number_input("HGB (Hemoglobin)", min_value=0.0, format="%.2f")

# Prediction button
if st.button("Predict"):
    input_data = np.array([[age, rbc, pcv, mcv, mch, mchc, rdw, tlc, plt, hgb]])
    prediction = model.predict(input_data)[0]
    result = "Anemic" if prediction == 1 else "Not Anemic"
    st.success(f"Prediction: **{result}**")
