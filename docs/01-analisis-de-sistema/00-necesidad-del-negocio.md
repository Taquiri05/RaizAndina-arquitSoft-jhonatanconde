# Necesidad del negocio

| Elemento | Descripción |
|---|---|
| Caso de estudio | Raíz Andina: cadena de restaurantes con 3 sedes en Ayacucho que necesita un Sistema Integral de Pedidos y Gestión. |
| Problema | Cada sede debe atender pedidos, pagos y cocina sin una vista común: hay riesgo de demoras, pedidos perdidos o duplicados, cobros sin confirmar y poco control consolidado del negocio, sobre todo en hora punta. |
| Objetivo del sistema | Permitir que el cliente consulte la carta, pida y pague en línea desde cualquier sede; que la cocina reciba solo pedidos pagados y avance su estado; y que los administradores gestionen su sede y el negocio completo. |
| Actores | Cliente, Personal de Cocina, Administrador de Sede y Súper Administrador. |
| Necesidades funcionales | Carta digital por sede, pedidos (delivery o recojo), pagos en línea, panel de cocina, reservas, fidelización, inventario y administración multisede (ver requisitos funcionales). |
| Necesidades de calidad | Rapidez en hora punta, seguimiento en tiempo real, pagos sin duplicados, datos aislados por sede y posibilidad de crecer sin reescribir el sistema (ver atributos de calidad). |
| Alcance | Un MVP con el flujo completo de un pedido (autenticación, menú, pedidos, pagos y cocina) y un incremento con el resto de módulos. |

## De la necesidad a la arquitectura

| Necesidad del negocio | Atributo de calidad | Driver | Decisión (ADR) |
|---|---|---|---|
| Atender a cientos de clientes a la vez en las 3 sedes | AC01 Rendimiento, AC02 Escalabilidad | DA01 | ADR-001, ADR-003 |
| Que cliente y cocina vean el estado del pedido al instante | AC03 Tiempo real | DA02 | ADR-008 |
| Cobrar una sola vez y no perder ningún pago | AC06 Integridad | DA03 | ADR-004, ADR-006, ADR-007 |
| Que cada sede vea solo sus datos | AC05 Seguridad | DA04 | ADR-005 |
| Crecer hasta 9 módulos sin reescribir el sistema | AC07 Modificabilidad | DA05 | ADR-001, ADR-002, ADR-010 |
| Cambiar de proveedores (pasarela de pago, correo, imágenes) sin romper el sistema | AC07 Modificabilidad | DA06 | ADR-004 |
| Que la interfaz web y el backend se comuniquen de forma clara | AC07 Modificabilidad | DA07 | ADR-011 |