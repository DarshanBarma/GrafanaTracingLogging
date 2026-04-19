from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get('/data')
def fetch_data():
    return {'data': "This is a data"}

@app.post('/[id]')
def post_data(id):
    for i in id:
        return