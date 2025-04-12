from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()
model = pickle.load(open("model.pkl", "rb"))

@app.get("/")
def read_root():
    return {"message": "ML Model API is running!"}

@app.post("/predict")
def predict(features: list):
    prediction = model.predict(np.array([features]))
    return {"prediction": int(prediction[0])}
