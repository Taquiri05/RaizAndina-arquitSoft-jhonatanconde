# Decisiones arquitectónicas (ADR)

ADR (Architecture Decision Record) documenta las decisiones importantes tomadas durante el diseño de la arquitectura de Raíz Andina, junto con su justificación.

| ID | Decisión arquitectónica | Driver relacionado | Justificación | Resultado |
|---|---|---|---|---|
| ADR-001 | Monolito modular | DA01 – Escalabilidad; DA05 – Modificabilidad | Organizar las funcionalidades en módulos independientes dentro de una misma aplicación desplegable, en vez de microservicios, para mantener un sistema simple de operar y de escalar. | Módulos de Menú Digital, Pedidos, Pagos, Reservas de Mesas, Fidelización, Inventario, Administración Multisede, Notificaciones y Panel de Cocina (KDS), con Autenticación y Seguridad como componente transversal. |
| ADR-002 | Clean Architecture | DA06 – Modificabilidad | Separar las reglas del negocio de los detalles tecnológicos, para poder modificar un módulo sin afectar innecesariamente a los demás. | Dominio, Aplicación, Infraestructura y Presentación. |
| ADR-003 | Estrategia de caché | DA01 – Rendimiento y Escalabilidad | Reducir consultas repetitivas a la base de datos en los momentos de mayor demanda entre las 3 sedes. | Caché en Redis para la carta (menú digital) y otra información de consulta frecuente. |
| ADR-004 | Integración de pagos mediante interfaces y adaptadores | DA03 – Pagos asíncronos; DA06 – Modificabilidad | Desacoplar los casos de uso del proveedor de pagos, para verificar y confirmar pagos de forma idempotente sin depender directamente de Mercado Pago. | Adaptador de Mercado Pago aislado en un solo módulo; el mismo criterio se aplica a Cloudinary y al servicio de correo. |
| ADR-005 | Autenticación con JWT que incluye rol y sede, y control de acceso (RBAC) en el backend | DA04 – Aislamiento por sede | Mantener el backend sin estado y filtrar automáticamente los datos por rol y sede; un administrador nunca ve datos de otra sede, aunque el cliente envíe otro identificador. | Token de acceso corto con token de refresco, revocación al cerrar sesión, control de rol y de alcance por sede, y límite de intentos de inicio de sesión. |
| ADR-006 | Confirmación de pagos con webhook idempotente y conciliación periódica | DA03 – Pagos asíncronos | Los webhooks pueden fallar o llegar duplicados, por lo que no se confía solo en ellos: cada notificación se verifica, se registra una sola vez y, si no llega, una tarea periódica consulta el estado a la pasarela. | Registro de eventos con identificador único, verificación contra la pasarela, confirmación en una sola transacción y tarea periódica de conciliación como respaldo. |
| ADR-007 | Precios congelados en el detalle del pedido | DA03 – Pagos e integridad | Mantener correctos el historial y los reportes aunque el administrador cambie el precio de un producto después de vendido. | Cada línea de pedido guarda el nombre y el precio del momento de la compra. |
| ADR-008 | Tiempo real con Socket.IO y salas por sede y por pedido | DA02 – Tiempo real | Cada actor recibe solo los eventos que le corresponden (su pedido o su sede), sin que el cliente elija su propia sala. | Salas por pedido y por sede (cocina), eventos de nuevo pedido y cambio de estado; Redis como canal entre réplicas cuando haya más de una. |
| ADR-009 | MySQL 8.0 como base de datos única | RC03 – Base de datos | Se evaluó PostgreSQL, pero se elige MySQL por ser una base relacional madura, suficiente para el volumen del sistema y compatible con SQLAlchemy. | Una sola base MySQL como fuente de verdad; Redis solo guarda información reconstruible. |
| ADR-010 | Una sola aplicación web (SPA) con tres experiencias según el rol | DA05 – Modificabilidad | Mantener un único proyecto de frontend en vez de tres aplicaciones separadas. | SPA en React con experiencias de cliente, administración y cocina, protegidas por rol. |
| ADR-011 | API REST en JSON como contrato entre la SPA y el backend | DA07 – API REST | Un contrato único, simple y conocido, que cualquier cliente web puede consumir y que separa el frontend del backend. | Recursos por entidad (sedes, productos, pedidos, pagos), respuestas en JSON, errores con códigos HTTP y control de acceso por rol en cada ruta. |

## Trazabilidad driver → decisión

| Driver | Decisiones que lo atienden |
|---|---|
| DA01 | ADR-001, ADR-003 |
| DA02 | ADR-008 |
| DA03 | ADR-004, ADR-006, ADR-007 |
| DA04 | ADR-005 |
| DA05 | ADR-001, ADR-010 |
| DA06 | ADR-002, ADR-004 |
| DA07 | ADR-011 |
| RC03 | ADR-009 |