from fastapi import FastAPI
from app.data.collector import get_cbond_data

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "CBond-Agent Running"
    }

@app.get("/market")
def market():
    df = get_cbond_data()
    return df.to_dict(orient="records")
