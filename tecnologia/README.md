# Tecnología

## Tecnologías definidas para Raíz Andina

| Capa | Tecnología | Origen |
|---|---|---|
| Backend | Python, Flask, SQLAlchemy y Flask-JWT-Extended | RC01 |
| Frontend | React, Vite, Tailwind y GSAP/ScrollTrigger | RC02 |
| Base de datos | MySQL 8.0 | RC03 |
| Caché, colas y tiempo real | Redis (Upstash) y Socket.IO | RC04 |
| Pagos e imágenes | Mercado Pago y Cloudinary | RC05 |
| Contenedores | Docker | AC10 – Portabilidad |
| Monitoreo de errores | Sentry | AC09 – Observabilidad |

## Ejemplo de código del enfoque Clean Architecture

La carpeta `ejemplo-clean-architecture/` es un **ejemplo didáctico** del enfoque elegido (ADR-002). No es el código del sistema: muestra, con el flujo pedido → pago → cocina del Nivel 4 del modelo C4, cómo se separan las capas y cómo se cambia de proveedor de pagos sin tocar las reglas del negocio (ADR-004).

```
ejemplo-clean-architecture/
├── dominio/                 ← EL CENTRO. No importa Flask ni ningún proveedor.
│   ├── pedido.py                entidades Pedido y DetallePedido; regla "solo hacia adelante"
│   └── pasarela_de_pago.py      contrato PasarelaDePago: cobrar() y consultar_pago()
├── aplicacion/              ← CASO DE USO. Solo conoce el dominio.
│   └── servicio_de_pagos.py     pagar y confirmar el pago sin procesar dos veces un aviso
├── infraestructura/         ← ADAPTADORES. Intercambiables.
│   ├── adaptador_mercado_pago_simulado.py
│   └── adaptador_otra_pasarela_simulado.py   otro proveedor, mismo contrato
├── presentacion/            ← RUTAS REST (Flask)
│   └── rutas_de_pagos.py
└── demo.py                  ensambla las capas y recorre el flujo
```

### Regla de dependencia

Las importaciones apuntan siempre hacia el centro: `presentacion` → `aplicacion` → `dominio` ← `infraestructura`. El dominio no importa nada de las otras capas.

### Ejecutar el ejemplo

```bash
cd tecnologia/ejemplo-clean-architecture
python demo.py
```

No necesita base de datos, credenciales ni conexión a internet: los adaptadores son simulados. La demo recorre el flujo dos veces, primero con Mercado Pago y luego con otra pasarela, sin cambiar el dominio ni el caso de uso. Solo `presentacion/rutas_de_pagos.py` necesita Flask.