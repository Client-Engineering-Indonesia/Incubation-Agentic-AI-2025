import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

class ModelRequest(BaseModel):
    forecast_window: int = 3


# Retrieve API key
API_KEY = os.getenv("WATSONX_API_KEY")
if not API_KEY:
    raise ValueError("Missing WATSONX_API_KEY in environment variables")

# Get authentication token
def get_auth_token():
    response = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data={"apikey": API_KEY, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"},
    )
    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Failed to get authentication token")
    return response.json()["access_token"]

# Prediction endpoint
@app.post("/predict")
def predict(request: ModelRequest):
    token = get_auth_token()
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    
    payload = {
        "input_data": [
            {"id": "observations", "values": []},
            {"id": "supporting_features", "values": []},
        ]
    }
    
    response = requests.post(
        os.getenv("WATSONX_URL"),
        json=payload,
        headers=headers,
    )
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    predictions = response.json()

    data = [
    {"quantity": round(item[0][0]), "sales": round(item[0][1],2)}
    for item in predictions['predictions'][0]['values']
    ]

    df = pd.DataFrame(data)

    if request.forecast_window==1:
        df=df.head(2)

    if request.forecast_window==1:
        df=df.head(1)
    
    return {"predictions":df.to_dict(orient='records')}


