# Decisiones arquitectónicas (ADR)

ADR (Architecture Decision Record) documenta las decisiones importantes tomadas durante el diseño de la arquitectura de Raíz Andina, junto con su justificación.

| ID | Decisión arquitectónica | Driver relacionado | Justificación | Resultado |
|---|---|---|---|---|
| ADR-001 | Monolito modular | DA01 – Escalabilidad; DA05 – Modificabilidad | Organizar las funcionalidades en módulos independientes dentro de una misma aplicación desplegable, en vez de microservicios, dado el plazo y el alcance individual del proyecto. | Módulos de Menú Digital, Pedidos, Pagos, Reservas de Mesas, Fidelización, Inventario, Administración Multisede y Panel de Cocina (KDS), con Autenticación y Seguridad como componente transversal. |
| ADR-002 | Clean Architecture | DA07 – Modificabilidad | Separar las reglas del negocio de los detalles tecnológicos, para poder modificar un módulo sin afectar innecesariamente a los demás. | Dominio, Aplicación, Infraestructura y Presentación. |
| ADR-003 | Estrategia de caché | DA01 – Rendimiento y Escalabilidad | Reducir consultas repetitivas a la base de datos en los momentos de mayor demanda entre las 3 sedes. | Caché en Redis para la carta (menú digital) y otra información de consulta frecuente. |
| ADR-004 | Integración de pagos mediante interfaces y adaptadores | DA03 – Pagos asíncronos | Desacoplar los casos de uso del proveedor de pagos, para verificar y confirmar pagos de forma idempotente sin depender directamente de Mercado Pago. | Contrato de pagos y adaptador para Mercado Pago. |
