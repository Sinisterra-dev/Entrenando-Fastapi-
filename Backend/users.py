from fastapi import FastAPI
from pydantic import BaseModel


# Inicia el server: python -m uvicorn users:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1, name="Alexander", surname="Sinisterra", url="https://sinisterradev.com", age=30),
    User(id=2, name="Fabiola", surname="Moreno", url="https://fabiola.com", age=28),
    User(id=3, name="Yulieth", surname="Bravo", url="https://yb.com", age=25)
]
# Endpoint para obtener todos los usuarios (ejemplo de datos estáticos)
@app.get("/users_example")
async def usersexample():
    return [{"nombre": "Alexander", "apellido": "Sinisterra", "web": "https://sinisterradev.com"},
            {"nombre": "Fabiola", "apellido": "Moreno", "web": "https://fabiola.com"},
            {"nombre": "Yulieth", "apellido": "Bravo", "web": "https://yb.com"}]

@app.get("/users")
async def users():
    return users_list   

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    return list(users)[0]
    

             