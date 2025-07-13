# SGA-IE-JSMMC-AUTENTICACION-SERVICIO
Servicio o API creada para las peticiones del usuario y validacion de credenciales

| Método | Endpoint           | Descripción                      |
| ------ | ------------------ | -------------------------------- |
| POST   | `/register`        | Registro de nuevos usuarios      |
| POST   | `/login`           | Autenticación e inicio de sesión |
| GET    | `/users/info/{id}` | Obtener información del usuario  |
| POST   | `/logout`          | Cierre de sesión     |
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

## 📚 Endpoints Autenticacion y consulta

| Método | Ruta                                     | Descripción                                          | Requiere Token     | Parámetros de Entrada         | Respuesta de Salida                         |
|--------|------------------------------------------|------------------------------------------------------|--------------------|-------------------------------|---------------------------------------------|
| **POST** | `/auth/login`                            | Iniciar sesión                                       | ❌                 | `email`, `contrasena`          | `access_token`, `rol`, `id`, `email`, etc.  |
| **GET**  | `/`                                       | Ruta raíz de autenticación                           | ❌                 | Ninguno                        | Mensaje general de bienvenida               |
| **POST** | `/usuario/register`                      | Registrar nuevo usuario                              | ❌                 | Datos del usuario (JSON)       | Objeto del usuario registrado               |
| **GET**  | `/usuario/getUsers`                      | Obtener todos los usuarios                           | ✅ (Token válido)  | Ninguno                        | Lista de usuarios                           |
| **GET**  | `/admin/dashboard`                       | Vista de administrador                               | ✅ (Administrador) | Ninguno                        | Mensaje de bienvenida                       |
| **GET**  | `/profesor/`                             | Vista de profesor                                    | ✅ (Profesor)      | Ninguno                        | Mensaje de bienvenida                       |
| **GET**  | `/profesor/{id_profesor}`                | Obtener datos básicos del profesor                   | ✅ (Profesor)      | `id_profesor`                  | `id_profesor`, `especialidad`, etc.         |
| **GET**  | `/profesor/profesores/{id_profesor}`     | Obtener datos completos del profesor y usuario       | ✅ (Profesor)      | `id_profesor`                  | Datos combinados del profesor y usuario     |
| **GET**  | `/acudiente/`                            | Vista de acudiente                                   | ✅ (Acudiente)     | Ninguno                        | Mensaje de bienvenida                       |
| **GET**  | `/acudiente/{id_acudiente}`              | Obtener datos del acudiente por ID                   | ✅ (Acudiente)     | `id_acudiente`                 | Objeto del acudiente                        |

---

### 🧪 Ejemplo de autenticación


Request body
```json
{
  "email": "usuario@example.com",
  "contrasena": "tu_clave_secreta"
}
{
  "username": "usuario",
  "password": "contrasena"
}
```

Successful Response
```json
{
  "access_token": "string",
  "token_type": "string",
  "rol": "string",
  "correo": "string",
  "id": 0,
  "nombres": "string",
  "apellidos": "string",
  "id_profesor": 0  //Solo si es profesor
}
```

### 📋 Ejemplo de respuesta: /profesor/{id_profesor}
```json
{
  "id_profesor": 11,
  "id_usuario": 11,
  "especialidad": "Matemáticas",
  "es_director": true
}

```

### Ejemplo de respuesta: /profesor/profesores/{id_profesor}
```json
{
  "id_profesor": 1,
  "id_usuario": 10,
  "especialidad": "Matemáticas",
  "es_director": true,
  "nombres": "Ana",
  "apellidos": "Gómez",
  "tipo_documento": "CC",
  "documento_identidad": "12345678",
  "telefono": "1234567890",
  "email": "ana@example.com",
  "rol": "profesor",
  "estado": true,
  "fecha_creacion": "2024-01-01T00:00:00",
  "fecha_modificacion": "2024-01-01T00:00:00"
}
```

### 📋 Ejemplo de respuesta: /acudiente/{id_acudiente}
```json
{
  "direccion": "Calle 1 #1-11",
  "id_usuario": 30,
  "parentesco": "Padre",
  "id_acudiente": 1,
  "celular": "3001234567"
}
```

## 📚 Endpoints Administrativo

| Método | Ruta                                      | Descripción                                           | Requiere Token     | Parámetros de Entrada          | Respuesta de Salida                            |
|--------|-------------------------------------------|-------------------------------------------------------|--------------------|---------------------------------|------------------------------------------------|
| **POST** | `/admin/usuarios`                        | Crear un nuevo usuario                                | ✅ (Administrador)  | Datos del usuario (JSON)       | Mensaje de éxito, ID del usuario creado        |
| **PATCH** | `/admin/usuarios/{id_usuario}`          | Editar parcialmente los datos de un usuario           | ✅ (Administrador)  | ID de usuario, datos a actualizar (JSON) | Mensaje de éxito, usuario actualizado          |
| **PATCH** | `/admin/usuarios/{id_usuario}/estado`   | Cambiar el estado de un usuario (activo/inactivo)     | ✅ (Administrador)  | ID de usuario, estado (activo/inactivo) | Mensaje de éxito, estado del usuario actualizado |
| **DELETE** | `/admin/usuarios/{id_usuario}`         | Eliminar un usuario                                   | ✅ (Administrador)  | ID de usuario                   | Mensaje de éxito, usuario eliminado            |

---

### 🧪 Ejemplo de creación de usuario profesor


**Request body**:
```json
{
  "nombres": "Juan",
  "apellidos": "Pérez",
  "tipo_documento": "CC",
  "documento_identidad": "123343489",
  "telefono": "3001234567",
  "email": "juan.perez3@colegio.com",
  "contrasena": "claveSecreta123",
  "rol": "profesor",
  "datos_adicionales": {
    "especialidad": "Matemáticas",
    "es_director": true
  }
}
```
### 📋 Ejemplo de respuesta:

```json
{
  "mensaje": "Usuario creado correctamente",
  "id_usuario": 57
}
```
### 🧪 Ejemplo de creación de usuario administrador:

```json
{
  "nombres": "Juan",
  "apellidos": "Pérez",
  "tipo_documento": "CC",
  "documento_identidad": "1256789",
  "telefono": "3001234567",
  "email": "juan.perez5@colegio.com",
  "contrasena": "claveSecreta123",
  "rol": "administrador",
  "datos_adicionales": {}
}
```
### 📋 Ejemplo de respuesta:
```json
{
  "mensaje": "Usuario creado correctamente",
  "id_usuario": 58
}
```

### 🧪 Ejemplo de creación de usuario acudiente:

```json
{
  "nombres": "Juan",
  "apellidos": "Pérez",
  "tipo_documento": "CC",
  "documento_identidad": "154534589",
  "telefono": "3001234567",
  "email": "juan.perez9@colegio.com",
  "contrasena": "claveSecreta123",
  "rol": "acudiente",
  "datos_adicionales": {
    "parentesco": "Padre",
    "celular": "3007654321",
    "direccion": "Calle 123, Bogotá"
  }
}
```
### 📋 Ejemplo de respuesta:
```json
{
  "mensaje": "Usuario creado correctamente",
  "id_usuario": 59
}
```

### 🧪 Ejemplo de actualización parcial de usuario

Ingresas el id del usuario y despues los datos que quieres modificar:

```json
{
  "nombres": "Juan Carlos",
  "apellidos": "Pérez Gómez",
  "rol": "profesor",
  "datos_adicionales": {
    "especialidad": "Español"
  }
}
```
### 📋 Ejemplo de respuesta:
```json
{
  "mensaje": "Usuario actualizado correctamente"
}
```
### 🧪 Ejemplo de cambio de estado de usuario
Ingresas primero el id del usuario y el estado (Debe ser 'activo' o 'inactivo')

### 📋 Ejemplo de respuesta:
```json
{
  "mensaje": "Estado de usuario actualizado correctamente"
}
```

### 🧪 Ejemplo de elimininacion de usuario
Ingresas el id del usuario a eliminar

### 📋 Ejemplo de respuesta:
```json
{
  "mensaje": "Usuario eliminado correctamente"
}
```

## 🔧 Dependencias utilizadas
- fastapi

- uvicorn

- python-dotenv

- python-jose

- passlib[bcrypt]

