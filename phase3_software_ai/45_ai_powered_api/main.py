from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Req(BaseModel):
    text: str

@app.post("/predict")
def predict(req: Req):
    # tiny 'AI-ish' rule just as placeholder
    score = len(req.text)
    return {"length_score": score}
