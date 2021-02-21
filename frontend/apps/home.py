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
    selected_gender = create_custom_selectbox(title="Gender", options=['Woman', 'Man'])
    selected_relevent_experience = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    selected_enrolled_university = create_custom_selectbox(title="Are you currently enroled in a university?", options=['Yes', 'No'])
    
    selected_education_level = create_custom_selectbox(title="What is your education level?", options=['Master', 'Graduate'])
    # selected_ = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    # selected_ = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    # selected_ = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    # selected_ = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    # selected_ = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    # selected_ = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    # selected_ = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])
    # selected_ = create_custom_selectbox(title="Do you have a relevant experience?", options=['Yes', 'No'])


#   "gender": "0",
#   "relevent_experience": "1",
#   "enrolled_university": "1",
#   "education_level": "1",
#   "major_discipline": "1",
#   "experience": "1",
#   "company_size": "1",
#   "company_type": "1",
#   "last_new_job": "0",
#   "training_hours": "0",
#   "city_development_index": "0",
#   "city": "1"


    st.markdown("### What kind of job are you looking for?")
    
    st.markdown("### Our Advices")