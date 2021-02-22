import time

import uvicorn
from fastapi import FastAPI

import config
from typing_class import PersonData
from handle_inference import encode, inference


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API created by Seb and Thomas."}


@app.post("/{ai_model}")
async def predict_person_job_change(ai_model: str, person_data: PersonData):
    """
    Predict the probability of an candidate looking for a new job.
    """
    print("\n----- Handle Prediction -----")
    print(person_data)
    start = time.time()
    person_data_encoded = encode(person_data)
    (prediction_class, prediction_proba_0, prediction_proba_1) = inference(ai_model, person_data_encoded)

    return {"prediction_class": prediction_class, "prediction_proba_0": prediction_proba_0, "prediction_proba_1": prediction_proba_1, "time": time.time() - start}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
