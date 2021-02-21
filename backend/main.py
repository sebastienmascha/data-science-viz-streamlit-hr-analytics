import time
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

import config
import inference


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API created by Seb and Thomas."}


class PersonData(BaseModel):
    gender: str
    relevent_experience: str
    enrolled_university: str
    education_level: str
    major_discipline: str
    experience: str
    company_size: str
    company_type: str
    last_new_job: str
    training_hours: str
    city_development_index: Optional[str] = None
    city: Optional[str] = None


@app.post("/{ai_model}")
async def predict_person_job_change(ai_model: str, person_data: PersonData):
    """
    Predict the probability of an candidate looking for a new job.
    """
    model = config.STYLES[ai_model]
    start = time.time()
    prediction = inference.inference(model, person_data)

    return {"prediction": prediction, "time": time.time() - start}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
