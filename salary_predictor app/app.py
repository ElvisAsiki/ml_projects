import pickle
import numpy as np
import streamlit as st

# Load the model safely
try:
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file not found. Please check 'model.pkl'.")

# Title centered using columns
col0, col1, col2, col3, col4, col5, col6 = st.columns(7)
with col3:
    st.title("Salary Predictor")

# Subtitle
st.markdown("<h6 style='text-align: center;'>A simple web app to predict your estimated annual salary</h6>", unsafe_allow_html=True)

# Dropdown and input options
gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", 
            "Senior Financial Analyst", "Senior Software Engineer"]
job_idx = [0, 1, 10, 11, 20]  # Assumed encoding for job titles

# Collect user input
gender = st.radio('Select your gender', gen_list)
age = st.slider(' Select your age', 21, 55)
education = st.selectbox('Choose your education level', edu_list)
job = st.selectbox('Choose your job title', job_list)
experience = st.slider('Years of experience', 0.0, 25.0, 0.0, 0.5, "%1f")

# Prediction button
colA, colB, colC, colD, colE = st.columns(5)
with colC:
    predict_btn = st.button('Predict Salary')

# Run prediction
if predict_btn:
    try:
        inp1 = int(age)
        inp2 = float(experience)
        inp3 = int(job_idx[job_list.index(job)])
        inp4 = int(edu_list.index(education))
        inp5 = int(gen_list.index(gender))
        
        # Input array
        X = [inp1, inp2, inp3, inp4, inp5]
        salary = model.predict([X])

        # Display salary
        colX, colY, colZ = st.columns(3)
        with colY:
            st.success(f"Estimated Annual Salary: **${int(salary[0]):,}**")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
