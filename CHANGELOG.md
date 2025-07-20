# 📄 CHANGELOG

Todas las modificaciones importantes realizadas en el proyecto se documentan en este archivo.
---
## [1.0.12] - 2025-07-20
### ✅ Añadido

- Se implementó el endpoint `POST /acudiente/register` para registrar un acudiente a partir de un usuario existente con rol "acudiente".
- Se añadió el endpoint `GET /acudiente/get_by_document/{document_number}` para consultar los datos de un acudiente usando el número de documento.

---
## [1.0.11] - 2025-07-17
### ✅ Añadido

- Agregamos nuevos campos en la respuesta al consultar los usuarios, como el tipo de documento, el numero de documento y el telefono.
---
## [1.0.10] - 2025-07-16
### ✅ Añadido

- Se agrego la parte de observabilidad con prometheus.
---
## [1.0.9] - 2025-07-15
### ✅ Añadido

- Se agregaron nuevos endpoints para obtener todos los usuarios por rol.

---
## [1.0.8] - 2025-07-13
### ✅ Añadido
- Se agregaron nuevos endpoints para las funcionalidades del administrador.

---

## [1.0.7] - 2025-07-12
### ✅ Añadido
- Se agregaron pruebas unitarias para endpoints clave de autenticación y profesores.

---

## [1.0.6] - 2025-07-03
### 🛠 Cambiado
- Segmentación y estructuración lógica de la base de datos (se separaron modelos y responsabilidades).

---

## [1.0.5] - 2025-07-02
### 🔄 Refactorizado
- Se realizaron cambios en las rutas del módulo `profesor`.

---

## [1.0.4] - 2025-06-12
### ✅ Añadido
- Se añadió el ID del usuario y el correo electrónico (`email`) a la respuesta del login.

---

## [1.0.3] - 2025-06-12
### ✅ Añadido
- Se incluyó el campo `email` en la respuesta del login.

---

## [1.0.2] - 2025-06-11
### 🔧 Refactorizado
- Mejoras en la estructura interna del backend y enrutamiento general.

---

## [1.0.0] - 2025-06-07
### 🚀 Prototipo Inicial
- Primer prototipo funcional del sistema con autenticación básica y rutas principales.

