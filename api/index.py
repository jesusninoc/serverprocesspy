import psutil
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
async def hola():
    # Obtener una lista de todos los procesos del sistema
    lista_procesos = []
    for proceso in psutil.process_iter():
        try:
            info = proceso.as_dict(attrs=['pid', 'name', 'username'])
            lista_procesos.append(info)
        except psutil.NoSuchProcess:
            pass
    
    return {"message": "Hola, Mundo", "procesos": lista_procesos}
