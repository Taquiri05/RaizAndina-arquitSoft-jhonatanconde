# Escenarios de atributos de calidad

Cada escenario convierte uno de los atributos de calidad (`04-atributos-de-calidad.md`) en una condición medible, con la estructura de 6 partes: fuente del estímulo, estímulo, artefacto, entorno, respuesta esperada y medida de la respuesta. Se agrega la verificación (cómo se comprueba).

Las medidas son metas técnicas del proyecto y se ajustan si la evidencia lo exige.

## EQ-01. Rendimiento

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC01 – Rendimiento |
| **Driver relacionado** | DA01 |
| **ADR relacionado** | ADR-001, ADR-003 |
| **Fuente del estímulo** | Clientes de las 3 sedes |
| **Estímulo** | Abren la carta de su sede y confirman pedidos, a un ritmo de 50 pedidos por minuto. |
| **Artefacto** | Módulos Menú Digital y Pedidos, a través de la API REST. |
| **Entorno** | Operación normal en hora punta, con cientos de clientes conectados. |
| **Respuesta esperada** | La carta se muestra rápido y cada pedido se registra con los precios del momento, listo para pagar. |
| **Medida de la respuesta** | Carta con 95 % de las consultas en 500 ms o menos; creación de pedido con 95 % en 1,5 s o menos; 0 pedidos perdidos y menos del 1 % de errores. |
| **Verificación** | Prueba de carga que registre tiempos de respuesta, errores y pedidos creados. |

## EQ-02. Escalabilidad

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC02 – Escalabilidad |
| **Driver relacionado** | DA01 |
| **ADR relacionado** | ADR-001, ADR-005 |
| **Fuente del estímulo** | Clientes (por ejemplo, durante una promoción de fin de semana). |
| **Estímulo** | Los usuarios conectados suben de 200 a 1 000 en 10 minutos. |
| **Artefacto** | Backend (proceso web). |
| **Entorno** | Producción con escalado automático habilitado. |
| **Respuesta esperada** | Se agregan réplicas del backend sin intervención manual y el servicio sigue respondiendo. |
| **Medida de la respuesta** | Menos del 1 % de errores durante el pico y se mantienen las medidas de EQ-01. |
| **Verificación** | Aumentar progresivamente la carga y comparar errores, tiempos de respuesta y número de réplicas. |

## EQ-03. Tiempo real

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC03 – Tiempo real |
| **Driver relacionado** | DA02 |
| **ADR relacionado** | ADR-008 |
| **Fuente del estímulo** | Personal de Cocina |
| **Estímulo** | Pasa un pedido a "En preparación" desde el Panel de Cocina. |
| **Artefacto** | Módulo Notificaciones (Socket.IO) y pantalla del cliente. |
| **Entorno** | Operación normal con el cliente conectado, incluso con varias réplicas del backend. |
| **Respuesta esperada** | El cliente y el administrador ven el nuevo estado sin recargar la página. |
| **Medida de la respuesta** | 2 segundos o menos entre el toque en cocina y la actualización en pantalla (percentil 95); 100 % de eventos entregados. |
| **Verificación** | Medir el tiempo entre el cambio de estado y la recepción del evento en el cliente, con una y con varias réplicas. |

## EQ-04. Disponibilidad

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC04 – Disponibilidad |
| **Driver relacionado** | Ninguno de forma directa; se apoya en DA01 y DA03, porque la falla de un componente no debe perder pedidos ni pagos. |
| **ADR relacionado** | ADR-006, ADR-009 |
| **Fuente del estímulo** | Falla interna de la plataforma. |
| **Estímulo** | Una réplica del backend se detiene o el servicio de caché (Redis) deja de responder. |
| **Artefacto** | Backend y Redis. |
| **Entorno** | Operación normal. |
| **Respuesta esperada** | Las demás réplicas atienden; los pedidos y pagos se siguen guardando en MySQL, que es la fuente de verdad; los clientes de tiempo real se reconectan solos. |
| **Medida de la respuesta** | 0 pedidos y 0 pagos perdidos; reconexión en 10 segundos o menos; un pago cuyo webhook no llega se confirma en 7 minutos o menos mediante la conciliación. |
| **Verificación** | Detener una réplica y desconectar Redis durante una prueba, y comprobar que no se pierdan pedidos ni pagos. |

## EQ-05. Seguridad

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC05 – Seguridad |
| **Driver relacionado** | DA04 |
| **ADR relacionado** | ADR-005 |
| **Fuente del estímulo** | Administrador de la sede 1 (usuario autenticado). |
| **Estímulo** | Pide pedidos o productos enviando el identificador de la sede 2, o el identificador de un recurso de otra sede. |
| **Artefacto** | API REST y control de acceso por rol y sede. |
| **Entorno** | Operación normal. |
| **Respuesta esperada** | El backend ignora la sede enviada y usa la del token de sesión; el recurso ajeno se rechaza. |
| **Medida de la respuesta** | 0 datos de otra sede expuestos. |
| **Escenario complementario** | Una misma dirección intenta 100 inicios de sesión por minuto; tras 5 intentos por minuto el sistema responde "demasiadas solicitudes" y no afecta a usuarios legítimos de otras direcciones. |
| **Verificación** | Pruebas con usuarios de distintas sedes y roles que intenten acceder a datos ajenos, y una prueba de intentos repetidos de inicio de sesión. |

## EQ-06. Integridad

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC06 – Integridad |
| **Driver relacionado** | DA03 |
| **ADR relacionado** | ADR-004, ADR-006, ADR-007 |
| **Fuente del estímulo** | Mercado Pago (pasarela de pago). |
| **Estímulo** | La misma notificación de pago llega 2 o más veces. |
| **Artefacto** | Módulo Pagos. |
| **Entorno** | Operación normal. |
| **Respuesta esperada** | El pago se confirma una sola vez y el pedido pasa a cocina una sola vez. El stock y los puntos de fidelización tampoco se duplican. |
| **Medida de la respuesta** | 0 cobros, confirmaciones, descuentos de stock o acreditaciones de puntos duplicados. |
| **Verificación** | Enviar la misma notificación repetidas veces y comprobar que el pago y el pedido queden registrados una sola vez. |

## EQ-07. Modificabilidad

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC07 – Modificabilidad |
| **Driver relacionado** | DA05, DA06 |
| **ADR relacionado** | ADR-002, ADR-004 |
| **Fuente del estímulo** | Dueño del negocio. |
| **Estímulo** | Pide cambiar de pasarela de pago o agregar un método de pago nuevo. |
| **Artefacto** | Módulo Pagos y su adaptador de Mercado Pago. |
| **Entorno** | Tiempo de desarrollo. |
| **Respuesta esperada** | El cambio se limita al adaptador de la pasarela, al servicio de pagos, a la ruta del webhook y a la pantalla de pago. |
| **Medida de la respuesta** | 0 archivos modificados en los módulos de Menú, Autenticación o Cocina. |
| **Verificación** | Revisar los archivos modificados en el cambio y comprobar que queden dentro del alcance indicado. |

## EQ-08. Usabilidad

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC08 – Usabilidad |
| **Driver relacionado** | Ninguno de forma directa. |
| **ADR relacionado** | ADR-010 |
| **Fuente del estímulo** | Cliente nuevo, sin cuenta, y Personal de Cocina. |
| **Estímulo** | El cliente quiere hacer su primer pedido desde el celular; el cocinero quiere avanzar un pedido mientras cocina. |
| **Artefacto** | Aplicación web: experiencia de cliente y Panel de Cocina. |
| **Entorno** | Celular con pantalla pequeña y conexión móvil; tablet en la cocina en hora punta. |
| **Respuesta esperada** | El cliente elige sede, arma el carrito, confirma como invitado y paga; el cocinero avanza el estado con un solo toque. |
| **Medida de la respuesta** | Primer pedido en 3 minutos o menos y 5 pantallas o menos hasta el pago; 1 toque por cambio de estado en cocina. |
| **Verificación** | Prueba con usuarios reales cronometrando el primer pedido y contando pantallas y toques. |

## EQ-09. Observabilidad

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC09 – Observabilidad |
| **Driver relacionado** | Ninguno de forma directa. |
| **ADR relacionado** | Ninguno por ahora. |
| **Fuente del estímulo** | Backend o frontend. |
| **Estímulo** | Ocurre una excepción no controlada en producción. |
| **Artefacto** | Todo el sistema y la herramienta de monitoreo de errores (Sentry). |
| **Entorno** | Producción. |
| **Respuesta esperada** | El error se registra con su ruta, su traza y el usuario afectado, sin exponer datos sensibles; el usuario ve un mensaje genérico. |
| **Medida de la respuesta** | El error es visible en el monitoreo en 1 minuto o menos. |
| **Verificación** | Provocar un error controlado y comprobar el registro y el tiempo en que aparece. |

## EQ-10. Portabilidad

| Campo | Descripción |
|---|---|
| **Atributo relacionado** | AC10 – Portabilidad |
| **Driver relacionado** | Ninguno de forma directa. |
| **ADR relacionado** | Ninguno por ahora. |
| **Fuente del estímulo** | Desarrollador o evaluador. |
| **Estímulo** | Clona el repositorio en una máquina nueva. |
| **Artefacto** | Configuración de contenedores (Docker Compose). |
| **Entorno** | Máquina con Docker instalado. |
| **Respuesta esperada** | Un solo comando levanta el backend, el proceso de tareas, la base de datos y la caché con datos de ejemplo. |
| **Medida de la respuesta** | Sistema funcionando en 10 minutos o menos. |
| **Verificación** | Ejecutar el comando en una máquina limpia y cronometrar. |

## Trazabilidad

| Escenario | Atributo | Driver | ADR |
|---|---|---|---|
| EQ-01 | AC01 Rendimiento | DA01 | ADR-001, ADR-003 |
| EQ-02 | AC02 Escalabilidad | DA01 | ADR-001, ADR-005 |
| EQ-03 | AC03 Tiempo real | DA02 | ADR-008 |
| EQ-04 | AC04 Disponibilidad | (apoya DA01, DA03) | ADR-006, ADR-009 |
| EQ-05 | AC05 Seguridad | DA04 | ADR-005 |
| EQ-06 | AC06 Integridad | DA03 | ADR-004, ADR-006, ADR-007 |
| EQ-07 | AC07 Modificabilidad | DA05, DA06 | ADR-002, ADR-004 |
| EQ-08 | AC08 Usabilidad | – | ADR-010 |
| EQ-09 | AC09 Observabilidad | – | – |
| EQ-10 | AC10 Portabilidad | – | – |