import time

import uvicorn
from fastapi import FastAPI

import config
import inference


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API created by Seb and Thomas."}


@app.post("/{style}")
async def get_image(style: str, person_data: str):
    model = config.STYLES[style]
    start = time.time()
    prediction = inference.inference(model, person_data)

    return {"prediction": prediction, "time": time.time() - start}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
