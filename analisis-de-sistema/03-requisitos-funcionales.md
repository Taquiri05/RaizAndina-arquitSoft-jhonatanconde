# Requisitos funcionales

## Autenticación y Seguridad (transversal)

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-AUT-01 | El cliente puede registrarse con nombre, correo, teléfono y contraseña. | MVP |
| RF-AUT-02 | Los 4 actores inician sesión con correo y contraseña; el sistema emite un token con su rol y su sede. | MVP |
| RF-AUT-03 | El token de acceso expira y se renueva mediante un token de refresco, sin volver a pedir contraseña. | MVP |
| RF-AUT-04 | El usuario puede cerrar sesión; su token queda revocado. | MVP |
| RF-AUT-05 | El backend filtra automáticamente los datos según rol y sede; un administrador de sede nunca ve datos de otra sede. | MVP |
| RF-AUT-06 | El cliente puede comprar como invitado, indicando nombre, teléfono y correo, sin crear cuenta. | MVP |
| RF-AUT-07 | Recuperación de contraseña mediante un enlace de un solo uso enviado por correo. | Incremento |
| RF-AUT-08 | El súper administrador crea, desactiva y asigna sede a las cuentas de administrador y de cocina. | MVP |

## Menú Digital

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-MEN-00 | El cliente selecciona una sede antes de ver la carta o iniciar un pedido. | MVP |
| RF-MEN-01 | Mostrar la carta de una sede organizada por categorías (Platos Criollos, Chifas, Alitas, Tallarines, Caldos, Bebidas, Postres). | MVP |
| RF-MEN-02 | Cada producto muestra nombre, descripción, precio, foto y disponibilidad. | MVP |
| RF-MEN-03 | El administrador crea, edita y activa/desactiva productos de su sede (incluye productos nuevos o de temporada). | MVP |
| RF-MEN-04 | El administrador sube la foto del producto, almacenada en Cloudinary. | MVP |
| RF-MEN-05 | El administrador marca un producto como agotado manualmente. | MVP |
| RF-MEN-06 | Buscador por nombre y filtros por categoría, precio y etiqueta. | Incremento |
| RF-MEN-07 | Etiquetas por producto: más vendido, nuevo, picante. | Incremento |
| RF-MEN-08 | Plato recomendado del día, elegido por el administrador de sede. | Incremento |
| RF-MEN-09 | El cliente registrado marca productos como favoritos. | Incremento |
| RF-MEN-10 | El cliente registrado califica con 1–5 estrellas un producto que haya comprado. | Incremento |
| RF-MEN-11 | Efecto parallax en la presentación de la carta. | Incremento |

## Pedidos

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-PED-01 | El cliente agrega, quita y modifica cantidades en un carrito asociado a una sede. | MVP |
| RF-PED-02 | El cliente elige modalidad delivery (con dirección) o recojo en sede. | MVP |
| RF-PED-03 | Al confirmar, el pedido se registra en estado Recibido y entra a la cola de pedidos. | MVP |
| RF-PED-04 | El pedido recorre los estados Recibido → En preparación → Listo → Entregado (o Cancelado). | MVP |
| RF-PED-05 | El cliente ve el estado de su pedido en tiempo real. | MVP |
| RF-PED-06 | El sistema muestra un tiempo estimado de entrega según los pedidos en cola y la modalidad. | MVP |
| RF-PED-07 | El administrador ve y gestiona los pedidos de su sede, con filtros por estado y fecha. | MVP |
| RF-PED-08 | El cliente consulta su historial de pedidos. | Incremento |
| RF-PED-09 | El cliente registrado repite un pedido anterior con un clic. | Incremento |
| RF-PED-10 | El cliente cancela su pedido solo mientras está en estado Recibido. | Incremento |
| RF-PED-11 | Alerta al administrador si un pedido lleva demasiado tiempo sin cambiar de estado. | Incremento |

## Pagos

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-PAG-01 | El cliente paga en línea con Culqi: Yape, Plin, tarjeta o PagoEfectivo. | MVP |
| RF-PAG-02 | El sistema confirma el pago mediante el webhook de Culqi y actualiza el estado del pago. | MVP |
| RF-PAG-03 | Un pedido solo pasa a cocina cuando su pago está Confirmado. | MVP |
| RF-PAG-04 | Si el webhook no llega a tiempo, el sistema consulta el estado del cargo directamente a Culqi. | Incremento |
| RF-PAG-05 | El cliente recibe un comprobante digital del pago. | Incremento |
| RF-PAG-06 | El administrador emite reembolsos desde su panel, vía Culqi. | Incremento |

## Reservas de Mesas

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-RES-01 | El cliente consulta un calendario de disponibilidad por sede, fecha, hora y número de personas. | Incremento |
| RF-RES-02 | El sistema asigna automáticamente la mesa más pequeña que cubra el número de personas. | Incremento |
| RF-RES-03 | La reserva se confirma automáticamente y se notifica al cliente. | Incremento |
| RF-RES-04 | La reserva se cancela sola si el cliente no llega dentro de la tolerancia configurada. | Incremento |
| RF-RES-05 | Si no hay mesa disponible, el cliente se inscribe en lista de espera. | Incremento |
| RF-RES-06 | El cliente cancela su reserva antes de la hora reservada. | Incremento |
| RF-RES-07 | El administrador ve las reservas del día de su sede y marca llegada / no-show. | Incremento |
| RF-RES-08 | El administrador gestiona las mesas de su sede (número, capacidad, activa/inactiva). | Incremento |

## Fidelización

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-FID-01 | El cliente registrado acumula puntos por cada pedido pagado y entregado. | Incremento |
| RF-FID-02 | El cliente consulta su saldo de puntos, nivel e historial de movimientos. | Incremento |
| RF-FID-03 | El cliente canjea puntos por cupones de descuento aplicables a un pedido. | Incremento |
| RF-FID-04 | Niveles Bronce / Plata / Oro según puntos acumulados, con beneficios crecientes. | Incremento |
| RF-FID-05 | El súper administrador configura el catálogo de cupones y los umbrales de nivel. | Incremento |

## Inventario

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-INV-01 | El administrador registra insumos de su sede (nombre, unidad, stock actual, stock mínimo). | Incremento |
| RF-INV-02 | El administrador define la receta de cada producto (insumos y cantidades). | Incremento |
| RF-INV-03 | Al confirmarse el pago de un pedido, se descuentan automáticamente los insumos. | Incremento |
| RF-INV-04 | Alerta cuando un insumo baja de su stock mínimo. | Incremento |
| RF-INV-05 | Un producto se marca agotado automáticamente si algún insumo de su receta no alcanza. | Incremento |
| RF-INV-06 | El administrador registra reposiciones manuales de stock. | Incremento |
| RF-INV-07 | Historial de movimientos (entrada, salida por venta, ajuste) con usuario y fecha. | Incremento |

## Administración Multisede

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-ADM-01 | El súper administrador gestiona las sedes (nombre, dirección, horario, estado). | MVP |
| RF-ADM-02 | Dashboard de ventas con gráficos: por sede, por día, por producto, por método de pago. | Incremento |
| RF-ADM-03 | Reportes consolidados de las 3 sedes por rango de fechas. | Incremento |
| RF-ADM-04 | Exportar reportes a PDF y Excel. | Incremento |
| RF-ADM-05 | Registro de auditoría: quién hizo qué cambio, sobre qué entidad y cuándo. | Incremento |
| RF-ADM-06 | Parámetros configurables del sistema (tiempos, tolerancias, puntos). | Incremento |

## Notificaciones en tiempo real

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-NOT-01 | Nuevo pedido pagado → aviso inmediato al KDS y al administrador de la sede. | MVP |
| RF-NOT-02 | Cambio de estado del pedido → aviso al cliente. | MVP |
| RF-NOT-03 | Confirmación o fallo de pago → aviso al cliente. | Incremento |
| RF-NOT-04 | Eventos de reserva (confirmada, cancelada, mesa liberada) → aviso al cliente y administrador. | Incremento |
| RF-NOT-05 | Alertas operativas (stock mínimo, pedido demorado) → aviso al administrador. | Incremento |
| RF-NOT-06 | Cada notificación llega solo a los usuarios de la sede correspondiente. | MVP |

## Panel de Cocina (KDS)

| ID | Requisito funcional | Prioridad |
|---|---|---|
| RF-KDS-01 | Tablero con columnas por estado: Recibido, En preparación, Listo. | MVP |
| RF-KDS-02 | Cada tarjeta muestra número de pedido, productos, cantidades, notas, modalidad y tiempo transcurrido. | MVP |
| RF-KDS-03 | La cocina avanza el pedido de estado con un toque. | MVP |
| RF-KDS-04 | Los pedidos se ordenan por hora de confirmación de pago (el más antiguo primero). | MVP |
| RF-KDS-05 | El tablero se actualiza sin recargar la página. | MVP |
| RF-KDS-06 | El paso a Entregado lo registra el administrador de sede. | MVP |

## Relación entre historias de usuario y requisitos funcionales

| Historia de usuario | Requisitos funcionales relacionados |
|---|---|
| HU01 Registrarme como cliente | RF-AUT-01 |
| HU02 Iniciar sesión | RF-AUT-02, RF-AUT-03, RF-AUT-04 |
| HU03 Comprar como invitado | RF-AUT-06 |
| HU04 Gestionar cuentas del personal | RF-AUT-08 |
| HU05 Seleccionar sede | RF-MEN-00 |
| HU06 Ver la carta | RF-MEN-01, RF-MEN-02 |
| HU07 Gestionar productos de mi sede | RF-MEN-03, RF-MEN-04, RF-MEN-05 |
| HU08 Favoritos y calificación | RF-MEN-09, RF-MEN-10 |
| HU09 Armar mi carrito y confirmar pedido | RF-PED-01, RF-PED-02, RF-PED-03 |
| HU10 Seguir mi pedido en tiempo real | RF-PED-04, RF-PED-05, RF-PED-06 |
| HU11 Gestionar los pedidos de mi sede | RF-PED-07 |
| HU12 Pagar mi pedido en línea | RF-PAG-01 |
| HU13 Solo pedidos pagados llegan a cocina | RF-PAG-02, RF-PAG-03 |
| HU14 Ver los pedidos en el tablero | RF-KDS-01, RF-KDS-02, RF-KDS-04, RF-KDS-05 |
| HU15 Avanzar el estado de un pedido | RF-KDS-03 |
| HU16 Avisos solo para quien corresponde | RF-NOT-06 |
| HU17 Reservar una mesa | RF-RES-01, RF-RES-02, RF-RES-03 |
| HU18 Controlar las reservas del día | RF-RES-07 |
| HU19 Acumular puntos y ver mi nivel | RF-FID-01, RF-FID-02, RF-FID-04 |
| HU20 Descuento automático de stock | RF-INV-03, RF-INV-05 |
| HU21 Ver reportes consolidados | RF-ADM-02, RF-ADM-03 |
