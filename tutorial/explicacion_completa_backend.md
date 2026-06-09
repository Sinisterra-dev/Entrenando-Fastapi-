# Explicación completa del backend (para principiantes)

## 1) Qué es este proyecto
Este proyecto es una práctica inicial de **FastAPI** con endpoints básicos para responder texto y listar usuarios en memoria.

## 2) Qué problema resuelve
Sirve para aprender cómo crear rutas HTTP en FastAPI y cómo devolver datos JSON.

## 3) Qué tecnologías usa
- **Python**
- **FastAPI** (framework web)
- **Pydantic** (validación de datos)
- **Uvicorn** (servidor ASGI para correr FastAPI)

## 4) Cómo está organizado
Estructura real actual:
- `/Backend/main.py`
- `/Backend/users.py`
- `/type_hints.py`

No hay carpeta de base de datos, servicios, repositorios ni configuración central.

## 5) Qué hace cada carpeta y archivo importante
- **Backend/main.py**: crea una app FastAPI con rutas `/` y `/url`.
- **Backend/users.py**: crea otra app FastAPI independiente, define el modelo `User` y rutas CRUD parciales en memoria (solo lectura real).
- **type_hints.py**: archivo educativo de Python typing, no forma parte del backend HTTP.

## 6) Qué es FastAPI
FastAPI es un framework para construir APIs HTTP rápidas en Python, con validación automática y documentación Swagger/OpenAPI.

## 7) Qué es una ruta
Una ruta (endpoint) es una URL + método HTTP (GET/POST/etc.) que ejecuta una función.
Ejemplo: `GET /users`.

## 8) Qué es una petición HTTP
Es el mensaje que envía un cliente (browser, app, Postman) al backend para pedir o enviar datos.

## 9) Qué es una respuesta JSON
Es el formato de datos que devuelve la API, por ejemplo:
```json
{"id": 1, "name": "Alexander"}
```

## 10) Qué es CRUD
CRUD significa:
- **Create** (crear)
- **Read** (leer)
- **Update** (actualizar)
- **Delete** (eliminar)

En este proyecto solo hay lectura (`GET`) y no persistente.

## 11) Qué es una base de datos
Es el sistema donde guardas datos de forma persistente (PostgreSQL, MySQL, SQLite, etc.).

## 12) Cómo se conecta el backend con la base de datos
### Estado actual del proyecto
No hay conexión a base de datos.

### Cómo agregarla (guía recomendada)
1. Instalar librerías (ejemplo con SQLAlchemy + PostgreSQL):
   - `pip install sqlalchemy psycopg[binary] alembic`
2. Crear archivo de configuración (`app/core/config.py`) para leer `DATABASE_URL` desde variables de entorno.
3. Crear engine y session factory (`app/db/session.py`).
4. Crear modelos (`app/models/...`) y tablas.
5. Crear migraciones con Alembic.
6. Inyectar sesión en rutas con `Depends(get_db)`.
7. Hacer `commit/rollback/close` en flujo controlado.

Si quieres conectar a una BD Linux/local, usa una URL tipo:
- PostgreSQL: `postgresql://usuario:password` + `@host:5432/nombre_db`

## 13) Qué es autenticación
Es comprobar **quién eres** (ejemplo: login con email/contraseña).

## 14) Qué es autorización
Es comprobar **qué puedes hacer** después de autenticarte (ejemplo: admin sí puede borrar, user no).

## 15) Qué es JWT
JWT es un token firmado que identifica al usuario sin guardar sesión en servidor.
Partes:
- Header
- Payload (claims: `sub`, `exp`, roles, etc.)
- Signature (firma criptográfica)

## 16) Qué son los roles
Son perfiles de acceso (ejemplo: `admin`, `user`, `editor`).

## 17) Qué son los permisos
Son acciones permitidas por rol (crear usuario, borrar pedido, ver reportes, etc.).

## 18) Qué pasa cuando un usuario inicia sesión
### Estado actual
No existe endpoint de login.

### Flujo recomendado
1. Cliente envía credenciales.
2. Backend valida usuario y contraseña hash.
3. Backend genera JWT con expiración.
4. Cliente guarda token.
5. Cliente envía el header en formato `Authorization: Be` + `arer <token>` en rutas protegidas.

## 19) Qué pasa cuando un usuario hace una petición protegida
### Estado actual
No hay rutas protegidas.

### Flujo recomendado
1. Middleware/dependencia lee header `Authorization`.
2. Se verifica firma y expiración del JWT.
3. Se extrae usuario/roles del payload.
4. Se autoriza según permiso requerido.
5. Si falla: `401` (no autenticado) o `403` (sin permiso).

## 20) Qué pasa cuando el token es inválido o expira
- Token inválido/firma incorrecta: `401 Unauthorized`.
- Token expirado: `401 Unauthorized` + mensaje “token expirado”.
- El cliente debe volver a login o usar refresh token (si existe).

## 21) Qué pasa cuando se crea, lee, actualiza o elimina un registro
### Estado actual
No hay persistencia real. Solo lista en memoria en `Backend/users.py`.

### Flujo profesional esperado
1. Ruta recibe request.
2. Pydantic valida body/params.
3. Servicio aplica reglas de negocio.
4. Repositorio ejecuta query ORM/SQL.
5. Commit en éxito, rollback en error.
6. Respuesta JSON con código HTTP correcto.

## 22) Qué errores pueden aparecer y por qué
En código actual:
- `User not found` (respuesta manual en `search_user`).
- Posibles errores por estructura duplicada de funciones `root` en `main.py`.

Faltan manejadores globales de errores (`HTTPException`, validación estándar, trazabilidad).

## 23) Qué buenas prácticas debería seguir este backend
1. Unificar una sola app FastAPI principal.
2. Separar por capas: routers, services, repositories, models, schemas.
3. Agregar base de datos real y migraciones.
4. Implementar auth JWT + refresh token.
5. Usar hash de contraseñas (bcrypt/argon2).
6. Centralizar configuración con `.env`.
7. Manejo de errores consistente.
8. Logs estructurados.
9. Tests automáticos (pytest).
10. Linters/formatters (ruff/black).

## 24) Qué cosas faltan para que esto esté más profesional
- Arquitectura por capas
- Base de datos y migraciones
- Registro/login/JWT/roles/permisos
- Seguridad (CORS estricto, rate limiting, secret management)
- Versionado de API (`/api/v1`)
- Pruebas unitarias/integración
- CI/CD
- Observabilidad (logs, métricas, tracing)

## 25) Resumen del flujo completo paso a paso
### Flujo real actual
1. Cliente hace `GET` a una ruta.
2. FastAPI resuelve endpoint.
3. Pydantic valida parámetros tipados (por ejemplo `id: int`).
4. Función ejecuta lógica mínima (lista en memoria).
5. API responde JSON o texto.

### Flujo objetivo profesional (a implementar)
1. Cliente envía request.
2. Router recibe y valida entrada.
3. Dependencias ejecutan autenticación JWT.
4. Autorización valida rol/permiso.
5. Servicio procesa reglas.
6. Repositorio consulta base de datos.
7. Se hace commit/rollback.
8. Se mapea respuesta con schema.
9. Se devuelve JSON con código HTTP correcto.

---

## Análisis honesto del estado actual (muy importante)
- **No hay base de datos**.
- **No hay autenticación JWT**.
- **No hay autorización por roles o permisos**.
- **No hay endpoints de login/registro/logout**.
- **No hay middleware de seguridad**.
- **No hay separación de capas profesional**.
- **No hay tests automáticos configurados**.

Actualmente es un proyecto de aprendizaje inicial. Está bien para empezar, pero aún no es un backend productivo.
