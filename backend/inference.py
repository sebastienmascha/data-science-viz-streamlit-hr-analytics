import json

from joblib import load
import pandas as pd

import config
from main import PersonData


def inference(model: str, person_data):
    model_name = f"{config.MODEL_PATH}{model}.joblib"
    model = load(model_name) 

    json_object = json.loads(person_data.json())
    pairs = json_object.items()
    person_data_list = []
    for key, value in pairs:
        person_data_list.append(value)
    print(person_data)
    lst = [person_data_list] # E.g. [[40.   ,  0.776,  1.   ,  0.   ,  0.   ,  0.   , -1.   , 15., 75.   ,  0.   ,  6.   , 47.   ]] 
    X_to_test = pd.DataFrame(lst, columns =['city', 'city_development_index', 'gender', 'relevent_experience', 'enrolled_university', 'education_level', 'major_discipline', 'experience', 'company_size', 'company_type', 'last_new_job', 'training_hours'], dtype = float) 
    print(X_to_test)

    prediction = model.predict(X_to_test)
    print(str(prediction))
    return str(prediction)
