from fastapi import FastAPI
from pydantic import BaseModel


# Inicia el server: python -m uvicorn users:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# Instancia principal de la aplicación FastAPI.
app = FastAPI()


# Modelo de datos para representar un usuario.
# FastAPI usa este esquema para validar y serializar respuestas.
class User(BaseModel):
    # Identificador único del usuario.
    id: int
    # Nombre del usuario.
    name: str
    # Apellido del usuario.
    surname: str
    # URL del perfil o sitio web del usuario.
    url: str
    # Edad del usuario.
    age: int


# Lista en memoria con usuarios de ejemplo.
# Nota: estos datos no se guardan en base de datos.
users_list = [
    User(id=1, name="Alexander", surname="Sinisterra", url="https://sinisterradev.com", age=30),
    User(id=2, name="Fabiola", surname="Moreno", url="https://fabiola.com", age=28),
    User(id=3, name="Yulieth", surname="Bravo", url="https://yb.com", age=25)
]

# Endpoint para obtener todos los usuarios (ejemplo de datos estáticos)
@app.get("/users_example")
async def usersexample():
    # Devuelve una lista fija de diccionarios (demo simple).
    return [{"nombre": "Alexander", "apellido": "Sinisterra", "web": "https://sinisterradev.com"},
            {"nombre": "Fabiola", "apellido": "Moreno", "web": "https://fabiola.com"},
            {"nombre": "Yulieth", "apellido": "Bravo", "web": "https://yb.com"}]


# Endpoint para obtener la lista completa de usuarios del arreglo en memoria.
@app.get("/users")
async def users():
    return users_list   


# Path parameter: busca un usuario por su id desde la ruta (/user/1, /user/2, etc.).
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query parameter: busca un usuario por id usando query string (/user/?id=1).
@app.get("/user/")
async def user(id: int):
    return search_user(id)  
   

# Función auxiliar para encontrar un usuario por id dentro de users_list.
def search_user(id: int):
    # Filtra los usuarios cuyo id coincide con el recibido.
    users = filter(lambda user: user.id == id, users_list)
    try:
        # Retorna el primer resultado encontrado.
        return list(users)[0]
    except:
        # Si no hay coincidencias, responde con un mensaje de error.
        return {"error": "User not found"}
    

             