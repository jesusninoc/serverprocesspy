from fastapi import FastAPI

app = FastAPI()

@app.post("/api/")
async def hola():
    return {"message": "Hola, Mundo"}
