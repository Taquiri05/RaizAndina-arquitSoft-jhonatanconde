# Patrones de diseño

Patrones de diseño que se aplican en Raíz Andina y el problema que resuelve cada uno.

## Patrones aplicados

| Patrón | Dónde se usa | Problema que resuelve |
|---|---|---|
| **Adapter** | Adaptadores de Mercado Pago, Cloudinary y correo | Cada proveedor externo habla su propio idioma. El adaptador lo traduce al vocabulario del sistema: por ejemplo, el de Mercado Pago convierte `approved`, `rejected` e `in_process` en éxito, fallo o pendiente; el de Cloudinary valida formato y tamaño antes de subir la foto. |
| **Strategy** | Interfaz de pasarela de pago | El servicio de pagos depende de una interfaz y no de Mercado Pago. Cambiar de pasarela o agregar un método de pago es escribir un adaptador nuevo que cumpla la interfaz (ADR-004). |
| **Application Factory** | Creación de la aplicación según el entorno | Crea la aplicación con la configuración del entorno (desarrollo, pruebas o producción). Por ejemplo, las rutas de apoyo para desarrollo solo se registran si el entorno no es producción. |
| **Decorator** | Control de acceso por rol y sede | Protege cada ruta con la lista de roles permitidos sin repetir la comprobación dentro de cada función. Se complementa con la verificación de sede, que limita los datos a la sede del token. |
| **Capa de servicios** | Servicios de cada módulo | Las rutas no contienen reglas de negocio: solo reciben la petición y llaman al servicio. Así la misma regla (por ejemplo, confirmar un pago) sirve al webhook y a cualquier otra ruta que la necesite. |
| **Validación de entrada (DTO)** | Esquemas de entrada | Los datos se revisan y se normalizan antes de llegar a las reglas de negocio. |
| **Publicador / Suscriptor** | Módulo Notificaciones (Socket.IO) | Quien cambia el estado de un pedido no conoce a quién le interesa: emite el evento y lo reciben la sala del pedido (el cliente) y la sala de la sede (la cocina de esa sede). |
| **Observer (eventos internos)** | Pago confirmado | Inventario y Fidelización reaccionan a un pago confirmado sin acoplarse al módulo de Pagos. |
| **Máquina de estados** | Servicio de Pedidos | Impide estados inválidos: solo se avanza, pasar a preparación exige el pago confirmado y `ENTREGADO` queda reservado a quien administra la sede. |
| **Receptor idempotente** | Rutas de Webhook y entidad WebhookEvento (identificador único) | Mercado Pago puede avisar varias veces. Cada notificación se procesa una sola vez, así que el pago no se confirma dos veces. |
| **Tarea en segundo plano** | Cancelación de pedidos vencidos (RQ sobre Redis) | Cancela los pedidos cuyo pago venció sin bloquear las peticiones de los clientes. |

## Cómo funciona cada patrón

| Patrón | En pocas palabras |
|---|---|
| Adapter | El servicio de pagos pide cobrar; el adaptador arma la llamada a Mercado Pago, agrega el identificador de idempotencia y devuelve un resultado simple (éxito, fallo o pendiente). |
| Strategy | El servicio de pagos llama a la interfaz de pasarela; el adaptador configurado decide con qué proveedor se cobra. |
| Application Factory | Cada entorno crea su propia aplicación con su configuración, sin cambiar el código. |
| Decorator | `@rol_requerido("SUPER_ADMIN", "ADMIN_SEDE")` sobre una ruta rechaza con 403 a cualquier otro rol. |
| Publicador / Suscriptor | El cambio a `EN_PREPARACION` se emite una vez y llega al cliente y a la cocina a la vez. |
| Observer | El pago confirmado se publica una vez y cada módulo interesado (Inventario, Fidelización) lo atiende por su cuenta. |
| Receptor idempotente | Si la misma notificación llega dos veces, la segunda se reconoce por su identificador y se ignora. |

## Beneficio

Cambiar de pasarela de pago toca el adaptador, el servicio de pagos, la ruta del webhook y la pantalla de pago; los módulos de Menú, Autenticación y Cocina no se modifican (EQ-07). El control de acceso y la validación están en un solo lugar cada uno, en vez de repetidos en cada ruta.