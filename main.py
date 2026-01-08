from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Request(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/generate")
def generate(req: Request):
    return {
        "neutral": "OK, klingt gut.",
        "positiv": "Super 😄 klingt gut!",
        "emotional": "Alles klar 😊 meld dich später."
    }
