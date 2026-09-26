# Restricciones

| ID | Restricción | Descripción |
|---|---|---|
| RC01 | Backend | El backend se construye en Python + Flask + SQLAlchemy + Flask-JWT-Extended. |
| RC02 | Frontend | El frontend se construye en React + Vite + Tailwind + GSAP/ScrollTrigger. |
| RC03 | Base de datos | La base de datos es MySQL 8.0. |
| RC04 | Caché, colas y tiempo real | Redis (Upstash) se usa como caché y cola de trabajos; Socket.IO se usa para las notificaciones en tiempo real. |
| RC05 | Pagos e imágenes | Los pagos en línea se procesan con Culqi; las fotos de los productos se almacenan en Cloudinary. |
| RC06 | Estilo arquitectónico | El sistema se construye como un monolito modular en capas, con arquitectura cliente-servidor (no microservicios). |
| RC07 | Base de código | El proyecto parte del repositorio `polleria-lena-carbon`, adaptado y ampliado, y no se construye desde cero. |
| RC08 | Alcance del proyecto | Proyecto individual, con un plazo de 4 meses y metodología Spec-Driven Development (SDD): toda especificación se define antes de programarla. |
