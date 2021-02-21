from typing import List
import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title("HR Analytics")

    st.write("This is a sample home page in the mutliapp.")

    st.markdown("### What is your profil?")
    def create_custom_selectbox(title: str, options: List):
        custom_selectbox = st.selectbox(
            title,
            options)
        st.write('You selected:', custom_selectbox)
        return custom_selectbox
    def handle_map_dictionary(value, dictionary):
        try: value = dictionary[value]
        except Exception: 
            pass
        return value
    # Gender
    selected_gender = create_custom_selectbox(title="Gender", options=['Woman', 'Man', 'Other'])
    selected_gender = handle_map_dictionary(selected_gender, {'Woman':'Female', 'Man':'Male'})
    # Relevent Experience
    selected_relevent_experience = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    selected_relevent_experience = handle_map_dictionary(selected_relevent_experience, {'Yes':'Has relevent experience', 'No':'No relevent experience'})
    # Enrolled University
    selected_enrolled_university = create_custom_selectbox(title="Are you currently enroled in a university?", options=['Full-Time', 'Part-Time', 'No Enrollmennt'])
    selected_enrolled_university = handle_map_dictionary(selected_enrolled_university, {'Full-Time':'Full time course', 'Part-Time':'Part time course', 'No Enrollmennt':'no_enrollment'})
    # Education Level
    selected_education_level = create_custom_selectbox(title="What is your education level?", options=['Primary School', 'High School', 'Masters', 'Graduate', 'Phd'])
    # Major Discipline
    selected_major_discipline = create_custom_selectbox(title="What is your major discipline?", options=['STEM', 'Business Degree', 'Arts', 'Humanities', 'No Major', 'Other'])
    # Experience
    selected_experience = create_custom_selectbox(title="How many years of experience do you have?", options=['0.5', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0', '15.0', '16.0', '17.0', '18.0', '19.0', '20.0', '21.0', '22.0', '23.0', '24.0', '25.0', '26.0', '27.0', '28.0'])
    # company_size
    selected_company_size = create_custom_selectbox(title="How many employees are you in your current company?", options=['1-9', '10-49', '50-99', '100-500', '500-999', '1000-4999', '5000-9999', '10000-20000'])
    # Type of current employer
    selected_company_type = create_custom_selectbox(title="What kind of company are you working for?", options=['NGO', 'Public Sector', 'Early Stage Startup', 'Funded Startup', 'Pvt Ltd', 'Other'])
    # last_new_job
    selected_last_new_job = create_custom_selectbox(title="Difference in years between previous job and current job:", options=['No experience', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    selected_last_new_job = handle_map_dictionary(selected_enrolled_university, {'No experience': '0'})
    # training_hours
    selected_training_hours = st.text_input("How many training hours are you taking?", "65")
    # city_development_index
    selected_city_development_index = st.text_input("What is your city development index? (0 to 1)", "0.83")


    st.markdown("### What kind of job are you looking for?")
    
    st.markdown("### Our Advices")