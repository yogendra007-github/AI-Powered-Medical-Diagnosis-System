# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 22:12:40 2025

@author: yogen
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from transformers import pipeline

# Loading the models
diabetes_model = pickle.load(open('C:/Users/yogen/OneDrive/Desktop/medical desease system/saved models/diabetes_model (2).sav', 'rb'))
heart_diseases_model = pickle.load(open('C:/Users/yogen/OneDrive/Desktop/medical desease system/saved models/heart_disease_model.sav', 'rb'))
parkinsons_diseases_model = pickle.load(open('C:/Users/yogen/OneDrive/Desktop/medical desease system/saved models/parkinsons_model.sav', 'rb'))

# AI-powered medical advice chatbot
medical_chatbot = pipeline('text-generation', model='distilgpt2')

# Sidebar menu
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Medical Advice Chatbot'],
                           icons=['activity', 'heart', 'person', 'chat'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = float(st.text_input('Number of Pregnancies', 0))
        SkinThickness = float(st.text_input('Skin Thickness value', 0))
        DiabetesPedigreeFunction = float(st.text_input('Diabetes Pedigree Function value', 0))
    with col2:
        Glucose = float(st.text_input('Glucose Level', 0))
        Insulin = float(st.text_input('Insulin Level', 0))
        Age = float(st.text_input('Age of the Person', 0))
    with col3:
        BloodPressure = float(st.text_input('Blood Pressure value', 0))
        BMI = float(st.text_input('BMI value', 0))

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        diab_diagnosis = 'The person is Diabetic' if diab_prediction[0] == 1 else 'The person is Not Diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease prediction')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = float(st.text_input('Age', 0))
        cp = float(st.text_input('Chest Pain Type (cp)', 0))
        restecg = float(st.text_input('Resting Electrocardiographic Results (restecg)', 0))
        oldpeak = float(st.text_input('ST Depression Induced by Exercise (oldpeak)', 0))
        ca = float(st.text_input('Number of Major Vessels (ca)', 0))
    with col2:
        sex = float(st.text_input('Sex', 0))
        trestbps = float(st.text_input('Resting Blood Pressure (trestbps)', 0))
        thalach = float(st.text_input('Maximum Heart Rate Achieved (thalach)', 0))
        slope = float(st.text_input('Slope of the Peak Exercise ST Segment (slope)', 0))
        thal = float(st.text_input('Thalassemia (thal)', 0))
    with col3:
        chol = float(st.text_input('Serum Cholesterol (chol)', 0))
        fbs = float(st.text_input('Fasting Blood Sugar (fbs)', 0))
        exang = float(st.text_input('Exercise Induced Angina (exang)', 0))
        
    heart_diagnosis = ''

    if st.button('Heart Test Result'):
        heart_prediction = heart_diseases_model.predict([[age, sex, chol, cp, trestbps, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        heart_diagnosis = 'The person is having heart problems' if heart_prediction[0] == 1 else 'The person is Not having heart problems'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction')

    col1, col2, col3 = st.columns(3)
    with col1:
        fo = float(st.text_input('MDVP:Fo(Hz)', 0))
        fhi = float(st.text_input('MDVP:Fhi(Hz)', 0))
        flo = float(st.text_input('MDVP:Flo(Hz)', 0))
        jitter_percent = float(st.text_input('MDVP:Jitter(%)', 0))
        jitter_abs = float(st.text_input('MDVP:Jitter(Abs)', 0))
        rap = float(st.text_input('MDVP:RAP', 0))
        ppq = float(st.text_input('MDVP:PPQ', 0))
    with col2:
        ddp = float(st.text_input('Jitter:DDP', 0))
        shimmer = float(st.text_input('MDVP:Shimmer', 0))
        shimmer_db = float(st.text_input('MDVP:Shimmer(dB)', 0))
        apq3 = float(st.text_input('Shimmer:APQ3', 0))
        apq5 = float(st.text_input('Shimmer:APQ5', 0))
        apq = float(st.text_input('MDVP:APQ', 0))
        dda = float(st.text_input('Shimmer:DDA', 0))
    with col3:
        nhr = float(st.text_input('NHR', 0))
        hnr = float(st.text_input('HNR', 0))
        rpde = float(st.text_input('RPDE', 0))
        dfa = float(st.text_input('DFA', 0))
        spread1 = float(st.text_input('spread1', 0))
        spread2 = float(st.text_input('spread2', 0))
        d2 = float(st.text_input('D2', 0))
        ppe = float(st.text_input('PPE', 0))
        
        parkinsons_diagnosis = ''

        if st.button('pankinsons Test Result'):
            parkinsons_prediction = parkinsons_diseases_model.predict([[fo, ddp, nhr , fhi, shimmer,  hnr, flo, shimmer_db,rpde, jitter_percent,apq3,dfa, jitter_abs,apq5,spread1,rap,apq,spread2,ppq,dda,d2,ppe]])
            parkinsons_diagnosis = 'The person is having a problems' if parkinsons_prediction[0] == 1 else 'The person is Not having heart problems'
            st.success(parkinsons_diagnosis)

# Medical Advice Chatbot Page
if selected == 'Medical Advice Chatbot':
    st.title('Medical Advice Chatbot')
    user_input = st.text_input('Ask a medical question:')

    if st.button('Get Advice'):
        if user_input:
            response = medical_chatbot(user_input, max_length=100, num_return_sequences=1)
            st.write(response[0]['generated_text'])
        else:
            st.warning('Please enter a question.')

    
    
    
   
   
    