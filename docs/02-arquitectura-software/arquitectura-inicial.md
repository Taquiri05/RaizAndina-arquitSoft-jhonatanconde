# Arquitectura inicial del sistema

## Diagrama de arquitectura

![Arquitectura inicial de Raíz Andina](../../img/arquitectura-inicial.png)

## Descripción

La arquitectura inicial de Raíz Andina se organiza como un **monolito modular en capas**, con arquitectura cliente-servidor:

- **Presentación:** una sola aplicación React (SPA) con tres experiencias distintas según el rol (cliente, administrador/súper administrador, cocina), que consume la API REST y el canal Socket.IO del backend.
- **Lógica de negocio:** un solo backend Flask dividido internamente en módulos independientes con fronteras claras: Autenticación y Seguridad (transversal), Menú Digital, Pedidos, Pagos, Panel de Cocina (KDS), Notificaciones en tiempo real, Reservas de Mesas, Fidelización, Inventario y Administración Multisede.
- **Capa transversal (Redis):** absorbe los picos de tráfico mediante caché de la carta, cola de pedidos por sede, canal de eventos en tiempo real (Socket.IO), límite de peticiones (rate limiting) y revocación de tokens de sesión.
- **Datos:** toda la información persiste en una sola base de datos MySQL, que es la fuente de verdad del sistema.
- **Sistemas externos:** el módulo de Pagos se integra con Mercado Pago (pasarela de pago), el módulo de Menú se integra con Cloudinary (imágenes), y el sistema completo se apoya en un servicio de correo (recuperación de contraseña, comprobantes) y en Sentry (monitoreo de errores en producción).

Se eligió un monolito modular (en vez de microservicios) porque operaciones como "pedido + pago + descuento de stock" se resuelven mejor como una sola transacción de base de datos, y porque un único despliegue es más simple de operar para las 3 sedes. Cada módulo tiene una frontera clara, de modo que en el futuro podría extraerse como servicio independiente si el crecimiento del negocio lo justificara.