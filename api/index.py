from fastapi import FastAPI
import psutil

app = FastAPI()

@app.get("/api/procesos")
async def obtener_procesos():
    # Obtener una lista de todos los procesos del sistema
    lista_procesos = []
    for proceso in psutil.process_iter():
        try:
            info = proceso.as_dict(attrs=['pid', 'name', 'username'])
            lista_procesos.append(info)
        except psutil.NoSuchProcess:
            pass
    
    return {"procesos": lista_procesos}
