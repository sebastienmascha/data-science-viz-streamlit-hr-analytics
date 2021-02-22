from joblib import load
import pandas as pd

import config
from typing_class import PersonData


def encode(person_data: PersonData):
    data = [{'city': person_data.city, 'city_development_index': person_data.city_development_index, 'gender': person_data.gender, 'relevent_experience': person_data.relevent_experience, 'enrolled_university': person_data.enrolled_university, 'education_level': person_data.education_level, 'major_discipline': person_data.major_discipline, 'experience': person_data.experience, 'company_size': person_data.company_size, 'company_type': person_data.company_type, 'last_new_job': person_data.last_new_job, 'training_hours': person_data.training_hours}]
    person_data_encoded = pd.DataFrame.from_records(data)

    try:
        person_data_encoded['company_size'] = person_data_encoded['company_size'].replace({'10-49': int(30), '1-9': int(5), '10000-20000': int(15000), '50-99': int(75), '5000-9999': int(7500), '1000-4999': int(3000), '500-999': int(750), '100-500': int(300) })
        person_data_encoded['gender'] = person_data_encoded['gender'].replace({'Female':int(0),'Male':int(1) ,'Other':int(-1)})
        person_data_encoded['relevent_experience'] = person_data_encoded['relevent_experience'].replace({'No relevent experience':int(0),'Has relevent experience':int(1)})
        person_data_encoded['enrolled_university'] = person_data_encoded['enrolled_university'].replace({'no_enrollment':int(0),'Full time course':int(1) ,'Part time course':int(-1)})
        person_data_encoded['education_level'] = person_data_encoded['education_level'].replace({'Graduate':int(0),'Masters':int(1) ,'High School':int(-1), 'Phd':int(2),'Primary School':int(3)})
        person_data_encoded['company_type'] = person_data_encoded['company_type'].replace({'Pvt Ltd':int(0), 'Funded Startup':int(-1), 'Early Stage Startup':int(2), 'Other':int(3),'Public Sector':int(4), 'NGO':int(5)})
        person_data_encoded['major_discipline'] = person_data_encoded['major_discipline'].replace({'STEM':int(-1) ,'Business Degree':int(0), 'Arts':int(1) ,'Humanities':int(2) ,'No Major':int(3) ,'Other':int(4)})
    except TypeError:
        print("Already preprocessed: convert categorical variables to numerical")
    return person_data_encoded

def inference(model: str, person_data_encoded):
    model_name = f"{config.MODEL_PATH}{model}.joblib"
    model = load(model_name) 
    prediction_proba = model.predict_proba(person_data_encoded)[0]
    prediction_proba_0 = prediction_proba[0]
    prediction_proba_1 = prediction_proba[1]
    prediction_class = 1 if prediction_proba_1 >= 0.5 else 0
    print("Predicted Class: ", prediction_class)
    print("Probability for class 0 : ", prediction_proba_0)
    print("Probability for class 1 : ", prediction_proba_1)
    return (prediction_class, prediction_proba_0, prediction_proba_1)
