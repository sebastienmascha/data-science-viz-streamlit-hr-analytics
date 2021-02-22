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
    model = config.STYLES[ai_model]
    start = time.time()
    person_data_encoded = encode(person_data)
    prediction = inference(model, person_data_encoded)

    return {"prediction": prediction, "time": time.time() - start}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
