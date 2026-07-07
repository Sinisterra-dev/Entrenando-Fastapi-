# Entrenando FastAPI

Proyecto educativo para practicar fundamentos de backend con FastAPI.

## Propósito del proyecto
Aprender cómo definir rutas, recibir peticiones HTTP, validar datos básicos con Pydantic y devolver respuestas JSON.

## Stack tecnológico
- Python
- FastAPI
- Pydantic
- Uvicorn

## Estructura general
- `Backend/main.py`: app con endpoints básicos (`/`, `/url`).
- `Backend/users.py`: app con modelo `User` y endpoints de consulta de usuarios en memoria.
- `type_hints.py`: práctica de type hints en Python.
- `tutorial/explicacion_completa_backend.md`: guía pedagógica completa del backend.

## Cómo correr el proyecto
> Nota: hay dos apps FastAPI separadas en el repositorio.

1. Crear entorno virtual:
   - Linux/macOS: `python -m venv .venv && source .venv/bin/activate`
2. Instalar dependencias:
   - `pip install fastapi uvicorn pydantic`
3. Ejecutar app principal:
   - `python -m uvicorn Backend.main:app --reload`
4. Ejecutar app de usuarios (alternativa):
   - `python -m uvicorn Backend.users:app --reload`

## Variables de entorno
Actualmente no hay variables de entorno implementadas en el código.

Para profesionalizar el proyecto, se recomienda agregar:
- `DATABASE_URL`: cadena de conexión a base de datos.
- `JWT_SECRET_KEY`: clave para firmar tokens.
- `JWT_ALGORITHM`: algoritmo JWT (por ejemplo HS256).
- `ACCESS_TOKEN_EXPIRE_MINUTES`: expiración del token.

## Flujo básico de uso
1. Cliente envía petición HTTP a un endpoint.
2. FastAPI resuelve ruta y valida parámetros tipados.
3. Endpoint ejecuta lógica.
4. API devuelve respuesta (texto o JSON).

## Autenticación y base de datos (estado actual)
- No existe login, registro, logout ni JWT.
- No existe conexión a base de datos.
- Los usuarios de `Backend/users.py` viven en memoria (se pierden al reiniciar).

## Cómo probar endpoints
Con servidor en ejecución, abre:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

Endpoints disponibles según la app levantada:
- `GET /`
- `GET /url`
- `GET /users_example`
- `GET /users`
- `GET /user/{id}`
- `GET /user/?id=<numero>`

## Documentación detallada
Revisa la guía completa para principiantes en:
- `tutorial/explicacion_completa_backend.md`
