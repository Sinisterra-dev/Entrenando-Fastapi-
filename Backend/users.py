from fastapi import FastAPI
from pydantic import BaseModel


# Inicia el server: python -m uvicorn users:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

app = FastAPI()


@app.get("/users")
async def users():
    return [{"nombre": "Alexander", "apellido": "Sinisterra", "web": "https://sinisterradev.com"},
            {"nombre": "Fabiola", "apellido": "Moreno", "web": "https://fabiola.com"},
            {"nombre": "Yulieth", "apellido": "Bravo", "web": "https://yb.com"}]

            

            
             