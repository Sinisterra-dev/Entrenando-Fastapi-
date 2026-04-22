from fastapi import FastAPI

# Inicia el server: python -m uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

app = FastAPI()

@app.get("/")
async def root():
    return "Hola, FastApi"

@app.get("/url")
async def root():
    app = FastAPI()

    # Ruta raíz que retorna un saludo
    @app.get("/")
    async def root():
        return "Hola, FastApi"

    # Ruta que retorna la URL de GitHub
    @app.get("/url")
    async def root():
        return {"url_github": "Github.com/Sinisterra-dev"}
