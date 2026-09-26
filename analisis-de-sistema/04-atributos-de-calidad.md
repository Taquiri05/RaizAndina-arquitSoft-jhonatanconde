# Atributos de calidad

Escenario: en un fin de semana de alta demanda, las 3 sedes de Raíz Andina reciben cientos de clientes consultando la carta, armando pedidos y pagando en línea al mismo tiempo, mientras cocina y los administradores necesitan ver todo actualizado en tiempo real, sin perder ni duplicar ningún pedido.

| ID | Atributo de calidad | Escenario de calidad |
|---|---|---|
| AC01 | Rendimiento | La carta y la creación de pedidos deben responder rápido (carta servida desde caché, pedidos registrados en poco más de un segundo) incluso con cientos de clientes conectados entre las 3 sedes en hora punta. |
| AC02 | Escalabilidad | El sistema debe soportar el aumento de usuarios conectados (de 200 a 1 000) agregando réplicas del backend automáticamente, sin intervención manual. |
| AC03 | Tiempo real | Un cambio de estado de un pedido debe reflejarse en la pantalla del cliente y del panel de cocina en segundos, sin recargar la página, incluso con varias réplicas del backend activas. |
| AC04 | Disponibilidad | El sistema debe seguir funcionando aunque falle una réplica del backend o el servicio de caché (Redis), sin perder ningún pedido ni pago. |
| AC05 | Seguridad | Los datos de cada sede deben estar aislados por rol y por sede (un administrador nunca ve datos de otra sede), y el inicio de sesión debe resistir intentos de fuerza bruta. |
| AC06 | Integridad | Un mismo pago o webhook duplicado no debe generar dos cobros, dos descuentos de stock ni dos acreditaciones de puntos. |
| AC07 | Modificabilidad | Cambiar de pasarela de pago o agregar un módulo nuevo debe afectar solo los archivos de ese módulo o de su adaptador, sin tocar el resto del sistema. |
| AC08 | Usabilidad | Un cliente nuevo debe poder hacer su primer pedido desde el celular en pocos minutos y pocas pantallas; el personal de cocina debe poder avanzar un pedido con un solo toque. |
| AC09 | Observabilidad | Todo error ocurrido en producción debe quedar registrado con su ruta, su traza y el usuario afectado, sin exponer datos sensibles. |
| AC10 | Portabilidad | Todo el sistema (backend, worker, base de datos y caché) debe poder levantarse en una máquina nueva con un solo comando de Docker Compose. |
