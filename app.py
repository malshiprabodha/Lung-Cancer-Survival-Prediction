

import streamlit as st
import pandas as pd
import joblib


model = joblib.load("lung_cancer_model.pkl")

st.set_page_config(
    page_title="Lung Cancer Survival Prediction",
    page_icon="🫁",
    layout="centered"
)

st.title("🫁 Lung Cancer Survival Prediction")
st.write("Enter patient information to predict survival outcome.")

age = st.number_input("Age", min_value=1, max_value=120, value=60)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

country = st.number_input(
    "Country Code",
    min_value=0,
    value=0
)

cancer_stage = st.selectbox(
    "Cancer Stage",
    ["Stage I", "Stage II", "Stage III", "Stage IV"]
)

family_history = st.selectbox(
    "Family History",
    ["No", "Yes"]
)

smoking_status = st.selectbox(
    "Smoking Status",
    [
        "Never Smoked",
        "Former Smoker",
        "Current Smoker",
        "Passive Smoker"
    ]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

cholesterol_level = st.number_input(
    "Cholesterol Level",
    min_value=50,
    max_value=500,
    value=200
)

hypertension = st.selectbox(
    "Hypertension",
    ["No", "Yes"]
)

asthma = st.selectbox(
    "Asthma",
    ["No", "Yes"]
)

cirrhosis = st.selectbox(
    "Cirrhosis",
    ["No", "Yes"]
)

other_cancer = st.selectbox(
    "Other Cancer",
    ["No", "Yes"]
)

treatment_type = st.selectbox(
    "Treatment Type",
    [
        "Surgery",
        "Chemotherapy",
        "Radiation",
        "Combined"
    ]
)

treatment_duration = st.number_input(
    "Treatment Duration (Days)",
    min_value=0,
    max_value=5000,
    value=180
)


gender_map = {
    "Female": 0,
    "Male": 1
}

family_map = {
    "No": 0,
    "Yes": 1
}

binary_map = {
    "No": 0,
    "Yes": 1
}

stage_map = {
    "Stage I": 0,
    "Stage II": 1,
    "Stage III": 2,
    "Stage IV": 3
}

smoking_map = {
    "Current Smoker": 0,
    "Former Smoker": 1,
    "Never Smoked": 2,
    "Passive Smoker": 3
}

treatment_map = {
    "Chemotherapy": 0,
    "Combined": 1,
    "Radiation": 2,
    "Surgery": 3
}

# Prediction
if st.button("Predict Survival"):

    patient_data = pd.DataFrame([{
        "age": age,
        "gender": gender_map[gender],
        "country": country,
        "cancer_stage": stage_map[cancer_stage],
        "family_history": family_map[family_history],
        "smoking_status": smoking_map[smoking_status],
        "bmi": bmi,
        "cholesterol_level": cholesterol_level,
        "hypertension": binary_map[hypertension],
        "asthma": binary_map[asthma],
        "cirrhosis": binary_map[cirrhosis],
        "other_cancer": binary_map[other_cancer],
        "treatment_type": treatment_map[treatment_type],
        "treatment_duration": treatment_duration
    }])

    prediction = model.predict(patient_data)

    if prediction[0] == 1:
        st.success("✅ Predicted Outcome: Survived")
    else:
        st.error("⚠️ Predicted Outcome: Not Survived")