# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 00:15:17 2025

@author: Mahek Rana
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model

diabetes_model = pickle.load(open("diabetes_model.sav",'rb'))

heart_disease_model = pickle.load(open("heart_disease_model.sav",'rb'))



# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           
                           icons = ['activity','heart'],
                           
                           default_index=0)
    
    
# Diabetes Prediction page
if (selected == 'Diabetes Prediction'):
    
    # Page Title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from user
    # columns for input fields
    col1,col2,col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    
    with col2:
        Glucose = st.text_input("Glucose Level")
    
    with col3:
        BloodPressure = st.text_input("BloodPressure value")
    
    with col1:
        SkinThickness = st.text_input("SkinThickness Level")
   
    with col2:
        Insulin = st.text_input("Insulin Level")
    
    with col3:
        BMI = st.text_input("BMI value")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value") 
    
    with col2:
        Age = st.text_input("Age of the person")
    
    # code for prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
    
    
# Heart Disease Prediction
if (selected == 'Heart Disease Prediction'):
    
    # Page Title
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from user
    # columns for input fields
    col1,col2,col3 = st.columns(3)

    with col1:
        age = st.number_input("Age of Person", min_value=1, max_value=120)

    with col2:
        sex = st.number_input("Sex (1 = Male, 0 = Female)", min_value=0, max_value=1)

    with col3:
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)

    with col1:
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)")

    with col2:
        chol = st.number_input("Serum Cholesterol (mg/dl)")

    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)", min_value=0, max_value=1)

    with col1:
        restecg = st.number_input("Resting ECG Result (0-2)", min_value=0, max_value=2)

    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved")

    with col3:
        exang = st.number_input("Exercise Induced Angina (1 = Yes, 0 = No)", min_value=0, max_value=1)

    with col1:
        oldpeak = st.number_input("ST Depression Induced by Exercise", format="%.2f")

    with col2:
        slope = st.number_input("Slope of Peak Exercise ST Segment (0-2)", min_value=0, max_value=2)

    with col3:
        ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3)

    with col1:
        thal = st.number_input("Thal (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)", min_value=1, max_value=3)
        
    
    # code for prediction
    heart_diagnosis = ''
    
    # creating a button for prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person is not having heart disease'

    st.success(heart_diagnosis)
    