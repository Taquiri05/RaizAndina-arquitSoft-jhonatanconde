# Drivers arquitectónicos

| ID | Driver arquitectónico | Origen | ¿Por qué influye en la arquitectura? |
|---|---|---|---|
| DA01 | El sistema debe soportar entre 500 y 1 000 usuarios conectados a la vez entre las 3 sedes, con picos en horas punta. | AC01, AC02 – Rendimiento y Escalabilidad | Obliga a usar caché de la carta, cola de pedidos por sede y un backend sin estado (stateless) que pueda escalar horizontalmente. |
| DA02 | El estado de un pedido debe reflejarse en el cliente y en cocina en tiempo real, en pocos segundos. | AC03 – Tiempo real | Obliga a usar WebSockets (Socket.IO) con salas separadas por sede y por pedido, coordinadas mediante Redis cuando hay varias réplicas. |
| DA03 | Los pagos se confirman de forma asíncrona mediante webhooks de una pasarela externa (Culqi), que pueden fallar o llegar duplicados. | RC05 – Pagos, AC06 – Integridad | Obliga a verificar cada webhook, a que la confirmación del pago sea idempotente, y a una tarea de conciliación periódica como respaldo. |
| DA04 | Cada sede debe ver y modificar solo sus propios datos (menú, pedidos, inventario, reservas). | AC05 – Seguridad | Obliga a un control de acceso (RBAC) con rol y sede incluidos en el token de sesión, aplicado siempre en el backend. |
| DA05 | El proyecto es individual, con 4 meses de plazo, y debe poder crecer de un MVP a 9 módulos sin reescribirse. | RC08 – Alcance del proyecto, AC07 – Modificabilidad | Obliga a un monolito modular con módulos de fronteras y dependencias explícitas, en vez de microservicios. |
| DA06 | Se parte de un código heredado (Leña y Carbón) que hay que adaptar y ampliar, no reescribir desde cero. | RC07 – Base de código | Condiciona qué partes del código existente se reutilizan tal cual y cuáles se reemplazan por completo. |
