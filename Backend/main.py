from fastapi import FastAPI

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
