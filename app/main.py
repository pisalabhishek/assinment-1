from fastapi import FastAPI
from app.models import Policyholder, Claim
from app.services import add_policyholder, add_claim


app = FastAPI()

@app.post("/add_policyholder")
def register_policyholder(data: dict):
    holder = Policyholder(**data)
    add_policyholder(holder)
    return {"status": "Policyholder Registered"}

@app.post("/add_claim")
def register_claim(data: dict):
    claim = Claim(**data)
    add_claim(claim)
    return {"status": "Claim Registered"}