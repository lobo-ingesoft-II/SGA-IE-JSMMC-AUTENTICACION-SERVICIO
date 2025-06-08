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
