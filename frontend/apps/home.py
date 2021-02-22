from typing import List
import json

import streamlit as st
import requests


API_URL = "https://hr-api.smascha.ai"
# API_URL = "http://localhost:8080"


def app():
    st.title("HR Analytics")
    st.info("Enter your profile and receive feedback on your carreer! 🚀")

    st.markdown("### What is your profil?")
    def create_custom_selectbox(title: str, options: List, index: int = 0):
        custom_selectbox = st.selectbox(
            title,
            options,
            index,
        )
        st.markdown('You selected:' + custom_selectbox)
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
    selected_relevent_experience = create_custom_selectbox(title="Do you have a relevant experience?", options=['Has relevent experience', 'No relevent experience'])
    # Enrolled University
    selected_enrolled_university = create_custom_selectbox(title="Are you currently enroled in a university?", options=['Full-Time', 'Part-Time', 'No Enrollmennt'], index=1)
    selected_enrolled_university = handle_map_dictionary(selected_enrolled_university, {'Full-Time':'Full time course', 'Part-Time':'Part time course', 'No Enrollmennt':'no_enrollment'})
    # Education Level
    selected_education_level = create_custom_selectbox(title="What is your education level?", options=['Primary School', 'High School', 'Masters', 'Graduate', 'Phd'], index=3)
    # Major Discipline
    selected_major_discipline = create_custom_selectbox(title="What is your major discipline?", options=['STEM', 'Business Degree', 'Arts', 'Humanities', 'No Major', 'Other'])
    # Experience
    selected_experience = create_custom_selectbox(title="How many years of experience do you have?", options=['0.5', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0', '15.0', '16.0', '17.0', '18.0', '19.0', '20.0', '21.0', '22.0', '23.0', '24.0', '25.0', '26.0', '27.0', '28.0'], index=14)
    # company_size
    selected_company_size = create_custom_selectbox(title="How many employees are you in your current company?", options=['1-9', '10-49', '50-99', '100-500', '500-999', '1000-4999', '5000-9999', '10000-20000'], index=4)
    # Type of current employer
    selected_company_type = create_custom_selectbox(title="What kind of company are you working for?", options=['NGO', 'Public Sector', 'Early Stage Startup', 'Funded Startup', 'Pvt Ltd', 'Other'], index=4)
    # last_new_job
    selected_last_new_job = create_custom_selectbox(title="Difference in years between previous job and current job:", options=['No experience', '1', '2', '3', '4', '5', '6', '7', '8', '9'], index=1)
    selected_last_new_job = handle_map_dictionary(selected_last_new_job, {'No experience': '0'})
    # training_hours
    selected_training_hours = st.text_input("How many training hours are you taking?", "150")
    # city_development_index
    selected_city_development_index = st.text_input("What is your city development index? (0 to 1)", "0.62")
    # city
    selected_city = create_custom_selectbox(title="Where are you from?", options=['1',  '2',  '7',  '8',  '9',  '10',  '11',  '12',  '13',  '14',  '16',  '18',  '19',  '20',  '21',  '23',  '24',  '25',  '26',  '27',  '28',  '30',  '31',  '33',  '36',  '37',  '39',  '40',  '41',  '42',  '43',  '44',  '45',  '46',  '48',  '50',  '53',  '54',  '55',  '57',  '59',  '61',  '62',  '64',  '65',  '67',  '69',  '70',  '71',  '72',  '73',  '74',  '75',  '76',  '77',  '78',  '79',  '80',  '81',  '82',  '83',  '84',  '89',  '90',  '91',  '93',  '94',  '97',  '98',  '99',  '100',  '101',  '102',  '103',  '104',  '105',  '106',  '107',  '109',  '111',  '114',  '115',  '116',  '117',  '118',  '120',  '121',  '123',  '126',  '127',  '128',  '129',  '131',  '133',  '134',  '136',  '138',  '139',  '140',  '141',  '142',  '143',  '144',  '145',  '146',  '149',  '150',  '152',  '155',  '157',  '158',  '159',  '160',  '162',  '165',  '166',  '167',  '171',  '173',  '175',  '176',  '179',  '180'], index=16)
    
    st.markdown("### What kind of job are you looking for?")
    

    st.markdown("### Our Advices")
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    user_input_json = {
        "gender": selected_gender,
        "relevent_experience": selected_relevent_experience,
        "enrolled_university": selected_enrolled_university,
        "education_level": selected_education_level,
        "major_discipline": selected_major_discipline,
        "experience": selected_experience,
        "company_size": selected_company_size,
        "company_type": selected_company_type,
        "last_new_job": selected_last_new_job,
        "training_hours": selected_training_hours,
        "city_development_index": selected_city_development_index,
        "city": selected_city,
        }

    if st.button("Predict"):
        print("PRESSSSSS")
        response = requests.post(API_URL + '/rf_pipe', headers=headers, json=user_input_json)
        print(response.text)
        response_json = json.loads(response.text)
        if response_json['prediction'] == "1":
            st.success("Looking for a job change! 🤝🚀")
        else:
            st.warning('Not looking for job change! ⚠️')
        st.info("Our random forest model took {:.2f} second to process! ⚡🎉".format(response_json['time']))
        
