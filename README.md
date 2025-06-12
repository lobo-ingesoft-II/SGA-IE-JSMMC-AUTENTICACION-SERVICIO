# SGA-IE-JSMMC-AUTENTICACION-SERVICIO
Servicio o API creada para las peticiones del usuario y validacion de credenciales

| Método | Endpoint           | Descripción                      |
| ------ | ------------------ | -------------------------------- |
| POST   | `/register`        | Registro de nuevos usuarios      |
| POST   | `/login`           | Autenticación e inicio de sesión |
| GET    | `/users/info/{id}` | Obtener información del usuario  |
| POST   | `/logout`          | Cierre de sesión (opcional)      |
| GET    | `/roles`           | Listado de roles (admin)         |
| PUT    | `/users/{id}/role` | Asignación o cambio de rol       |


# SGA-IE-JSMMC-AUTENTICACION-SERVICIO
API REST desarrollada con FastAPI para gestionar roles y vistas según tipo de usuario: administrador, profesor y acudiente.

## 🚀 Cómo usar la API
### 1. Clonar el repositorio

```bash
git clone https://github.com/lobo-ingesoft-II/SGA-IE-JSMMC-AUTENTICACION-SERVICIO.git
cd SGA-IE-JSMMC-AUTENTICACION-SERVICIO
```
### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 3. Configurar base de datos
```python
DATABASE_URL = "mysql://usuario:contraseña@host:puerto/nombre_bd"
```
Completar con las credenciales que compartió jhoan 

### 4. Ejecutar la aplicación
Defini este servicio en el puerto 8009, tener presente de no haber otro servicio en este puerto
```bash
 uvicorn app.main:app --reload --port 8009
```
## 🔐 Autenticación y Seguridad
La API utiliza JWT para autenticación con OAuth2:

- Ruta de login: POST /auth/login

- Tiempo de expiración del token: 30 minutos

- Algoritmo JWT: HS256

- Parámetro de autenticación: Bearer Token

## 📚 Endpoints

| Método | Ruta                | Descripción         | Requiere Token     | Parámetros de Entrada | Respuesta de Salida       |
|--------|---------------------|---------------------|---------------------|------------------------|----------------------------|
| POST   | `/auth/login`       | Iniciar sesión      | ❌                  | `username`, `password` | `access_token` JWT         |
| GET    | `/admin/dashboard`  | Vista Admin         | ✅ (Admin)          | Ninguno                | Mensaje de bienvenida      |
| GET    | `/estudiante/`      | Vista Estudiante    | ✅ (Estudiante)     | Ninguno                | Mensaje de bienvenida      |
| GET    | `/profesor/`        | Vista Profesor      | ✅ (Profesor)       | Ninguno                | Mensaje de bienvenida      |
| GET    | `/acudiente/`       | Vista Acudiente     | ✅ (Acudiente)      | Ninguno                | Mensaje de bienvenida      |
| GET    | `/`                 | Ruta raíz (default) | ❌                  | Ninguno 

## 🧪 Ejemplo de autenticación

Request body
```bash
{
  "username": "usuario",
  "password": "contrasena"
}
```

Successful Response
```bash
{
  "access_token": "string",
  "token_type": "string",
  "rol": "string"
}
```

## 🔧 Dependencias utilizadas
- fastapi

- uvicorn

- python-dotenv

- python-jose

- passlib[bcrypt]

