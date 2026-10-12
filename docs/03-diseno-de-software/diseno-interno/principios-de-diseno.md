# Principios de diseño (SOLID)

Principios SOLID aplicados al diseño de Raíz Andina, con foco en el flujo de pedidos y pagos.

## Aplicados al flujo de pedidos y pagos

| Principio | Cómo se aplica en el diseño |
|---|---|
| **S — Responsabilidad única** | Cada componente tiene un solo motivo de cambio: el Adaptador de Mercado Pago solo habla con la pasarela, el servicio de fotos solo gestiona imágenes en Cloudinary, el Servicio de Auditoría solo registra cambios y el control de acceso solo decide permisos. |
| **O — Abierto/cerrado** | Cambiar de pasarela o agregar otro método de pago se resuelve con un adaptador nuevo que cumple la interfaz de pasarela de pago (ADR-004), sin editar las reglas de Pedidos ni el Servicio de Pagos. |
| **L — Sustitución de Liskov** | Cualquier adaptador de pasarela puede sustituir a otro: todos devuelven la misma forma de respuesta (éxito, fallo o pendiente), de modo que el Servicio de Pagos funciona igual con cualquiera. |
| **I — Segregación de interfaces** | La interfaz de pasarela de pago define solo lo que el servicio necesita (cobrar y consultar el estado de un pago). Cada módulo expone funciones pequeñas y cada ruta usa solo las que necesita, en vez de un servicio único gigante. |
| **D — Inversión de dependencias** | Los servicios dependen de la interfaz de pasarela de pago y no del proveedor concreto. Las credenciales de un proveedor se necesitan solo al usarlo, no al arrancar la aplicación. |

## Qué pasaría sin cada principio

| Sin el principio | Consecuencia |
|---|---|
| Sin SRP | Un solo componente para pedidos, pagos y cocina: un cambio en el tablero de cocina podría romper el cobro. |
| Sin OCP | Cada método de pago nuevo obligaría a reescribir el flujo de pedidos. |
| Sin DIP | No se podría probar el flujo de pago sin llamar a la pasarela real ni cambiar de proveedor sin editar las reglas de negocio. |

## Otros criterios de diseño

| Criterio | Aplicación |
|---|---|
| **El servidor manda, el cliente no** | La sede sale del token, no de lo que envía el cliente (EQ-05). El monto y el correo del pago los define el servidor: lo que envíe el cliente se ignora. |
| **Defensa en profundidad** | El webhook se verifica consultando el pago en Mercado Pago, y además se guarda el identificador de la notificación para no repetirla. |
| **Validar todo de una vez** | Al confirmar el pedido se comprueba la disponibilidad y la sede de todos los productos juntos, no uno por uno. |
| **No bloquear el negocio por la auditoría** | Si falla el registro de auditoría, la operación se completa y el fallo se registra en el log. |

## Relación con el enfoque arquitectónico

El sistema sigue un monolito modular en capas con una organización basada en Clean Architecture (`enfoque-arquitectonico.md`). Los principios S, I y O se aplican en los módulos y adaptadores, y D mediante la interfaz de pasarela de pago. La comparación con Arquitectura Hexagonal en ese documento deja la decisión explícita en el ADR-002.