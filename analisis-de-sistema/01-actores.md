# Actores

| Actor | ¿Qué necesita realizar? |
|---|---|
| Cliente | Elegir la sede de la cadena, consultar la carta digital, armar su carrito, realizar pedidos (delivery o recojo), pagar en línea, reservar mesa, acumular puntos de fidelización y consultar el estado de sus pedidos. Puede comprar como invitado, sin crear cuenta. |
| Personal de Cocina | Usar el Panel de Cocina (KDS) para ver los pedidos ya pagados de su sede y avanzar su estado de preparación. Es una cuenta compartida por sede, no una por cada cocinero. |
| Administrador de Sede | Gestionar el menú, los pedidos, el inventario y las reservas de su propia sede, y registrar la entrega final de los pedidos. Puede haber varios administradores por sede. |
| Súper Administrador | Gestionar y supervisar las 3 sedes de forma consolidada: cuentas del personal, datos de las sedes, reportes y parámetros generales del sistema. |
| Culqi (pasarela de pago) | Procesar los pagos (Yape, Plin, tarjeta, PagoEfectivo) y notificar su resultado al sistema mediante webhooks. |
| Cloudinary | Almacenar y servir las fotos de los productos subidas por los administradores de sede. |
| Servicio de correo | Enviar correos de recuperación de contraseña y comprobantes de pago. |
| Sentry | Registrar los errores del backend y del frontend ocurridos en producción. |
