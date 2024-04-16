import psutil
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
async def procesos():
    # Obtener una lista de todos los procesos del sistema
    lista_procesos = []
    for proceso in psutil.process_iter():
        try:
            info = proceso.as_dict(attrs=['pid', 'name'])
            lista_procesos.append(info)
        except psutil.NoSuchProcess:
            pass
    
    return {"procesos": lista_procesos}
