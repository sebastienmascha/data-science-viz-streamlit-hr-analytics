from joblib import load
import pandas as pd

import config


def inference(model: str, person_data: str):
    model_name = f"{config.MODEL_PATH}{model}.joblib"
    model = load(model_name) 

    print(person_data)
    lst = [[40.   ,  0.776,  1.   ,  0.   ,  0.   ,  0.   , -1.   , 15., 75.   ,  0.   ,  6.   , 47.   ]] 
    X_to_test = pd.DataFrame(lst, columns =['city', 'city_development_index', 'gender', 'relevent_experience', 'enrolled_university', 'education_level', 'major_discipline', 'experience', 'company_size', 'company_type', 'last_new_job', 'training_hours'], dtype = float) 
    print(X_to_test)

    prediction = model.predict(X_to_test)
    print(str(prediction))
    return str(prediction)
