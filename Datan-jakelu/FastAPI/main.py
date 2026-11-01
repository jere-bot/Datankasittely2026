from fastapi import FastAPI
import json
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/testi")
async def i():
    return {
        "henkilöt": [{
            "nimi": "Testi",
            "ikä": 45,
            "email": "testi@testi.fi"
        },
        {
            "nimi": "testi2",
            "ikä": 422,
            "email": "testi2@testi.fi"
        }],
        "tavarat":
        [{
            "id": 1,
            "nimi": "tavara1"
        },
        {
            "id": 2,
            "nimi": "tavara2"
        }]
    }