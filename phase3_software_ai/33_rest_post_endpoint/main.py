from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/echo")
def echo(item: Item):
    return {"received": item.text}
