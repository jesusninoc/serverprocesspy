from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
async def hola():
    return {"message": "Hola, Mundo"}
