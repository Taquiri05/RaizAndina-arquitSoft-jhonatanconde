# Raíz Andina — Análisis y arquitectura de software

## Nombre
Jhonatan Conde Taquiri

## Descripción
Proyecto académico del curso de Arquitectura de Software, que aplica el método de análisis y diseño de arquitectura (Guías 01 a 03) sobre el sistema real **Raíz Andina**: un Sistema Integral de Pedidos y Gestión para una cadena de restaurantes ficticia con 3 sedes en Ayacucho, que el estudiante viene construyendo como proyecto integrador individual del curso.

## Sistema de referencia

**Actores (4):** Cliente (invitado o registrado), Personal de Cocina, Administrador de Sede, Súper Administrador.

**Módulos (9 + 1 transversal):** Menú Digital, Pedidos, Pagos, Reservas de Mesas, Fidelización, Inventario, Administración Multisede, Notificaciones en tiempo real, Panel de Cocina (KDS), y el componente transversal de Autenticación y Seguridad.

**Stack de referencia:** backend en Python/Flask + SQLAlchemy, frontend en React + Vite + Tailwind, base de datos MySQL 8.0, Redis como caché y canal de eventos en tiempo real (Socket.IO), pasarela de pagos Mercado Pago, imágenes en Cloudinary.

## Curso
Arquitectura de Software (IS-488) — Ing. Lizbeth Jaico Quispe — Semestre 2026-II

## Guías de laboratorio cubiertas

| Guía | Contenido | Estado |
|---|---|---|
| Guía 01-02 | Análisis del sistema (actores, historias de usuario, requisitos, atributos de calidad, restricciones, drivers) y arquitectura inicial | ✅ |
| Guía 03 | Decisiones arquitectónicas (ADR), estilo arquitectónico y enfoque Clean Architecture | ✅ |

## Estructura del repositorio

```
RaizAndina-arquitSoft-jhonatanconde/
├── analisis-de-sistema/
│   ├── 01-actores.md
│   ├── 02-historias-del-usuario.md
│   ├── 03-requisitos-funcionales.md
│   ├── 04-atributos-de-calidad.md
│   ├── 05-restricciones.md
│   ├── 06-driver-arquitectonicos.md
│   └── 07-decisiones-arquitectonicas.md
├── arquitectura/
│   ├── arquitectura-inicial.md
│   ├── estilo-arquitectonico.md
│   └── enfoque/
│       └── enfoque-arquitectonico.md
├── .gitignore
└── README.md
```