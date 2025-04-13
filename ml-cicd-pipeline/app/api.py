from fastapi import FastAPI
import numpy as np
import pickle
import os

app = FastAPI()

model_path = "/app/model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model file not found at {model_path}")

model = pickle.load(open(model_path, "rb"))

@app.get("/")
def root():
    return {"message": "ML model is live!"}

@app.post("/predict")
def predict(features: list):
    prediction = model.predict(np.array([features]))
    return {"prediction": int(prediction[0])}
