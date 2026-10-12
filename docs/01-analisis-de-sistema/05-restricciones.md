# Restricciones

| ID | Restricción | Descripción |
|---|---|---|
| RC01 | Backend | El backend se construye en Python + Flask + SQLAlchemy + Flask-JWT-Extended. |
| RC02 | Frontend | El frontend se construye en React + Vite + Tailwind + GSAP/ScrollTrigger. |
| RC03 | Base de datos | La base de datos es MySQL 8.0. |
| RC04 | Caché, colas y tiempo real | Redis (Upstash) se usa como caché y cola de trabajos; Socket.IO se usa para las notificaciones en tiempo real. |
| RC05 | Pagos e imágenes | Los pagos en línea se procesan con Mercado Pago; las fotos de los productos se almacenan en Cloudinary. |
| RC06 | Estilo arquitectónico | El sistema se construye como un monolito modular en capas, con arquitectura cliente-servidor (no microservicios). |
| RC07 | Aplicación web | El sistema es una aplicación web cliente-servidor: los usuarios acceden desde el navegador (computador o celular), sin instalar nada. |
| RC08 | Control de versiones | El proyecto se versiona con Git y GitHub; este repositorio de documentación trabaja con las ramas `main` y `developer` y mensajes de commit bajo Conventional Commits. |
| RC09 | API REST | El backend expone una API REST en formato JSON, consumida por la SPA; el tiempo real se atiende por separado con Socket.IO. |