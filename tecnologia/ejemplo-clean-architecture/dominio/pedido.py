# =============================================================
# DOMINIO · Entidad Pedido
# =============================================================
# El centro del sistema. No importa Flask, SQLAlchemy ni
# Mercado Pago: solo contiene las reglas del negocio.

from dataclasses import dataclass, field

# Orden de los estados: el pedido solo puede avanzar hacia adelante.
ESTADOS = ["RECIBIDO", "EN_PREPARACION", "LISTO", "ENTREGADO"]


@dataclass
class DetallePedido:
    # Nombre y precio se congelan al pedir (ADR-007):
    # si la carta cambia después, el pedido no cambia.
    nombre_producto: str
    precio_unitario: float
    cantidad: int

    def subtotal(self) -> float:
        return self.precio_unitario * self.cantidad


@dataclass
class Pedido:
    id: int
    sede_id: int
    correo_cliente: str
    detalles: list[DetallePedido]
    estado: str = "RECIBIDO"
    estado_pago: str = "PENDIENTE"
    historial: list[str] = field(default_factory=lambda: ["RECIBIDO"])

    def total(self) -> float:
        return sum(d.subtotal() for d in self.detalles)

    def confirmar_pago(self) -> None:
        self.estado_pago = "CONFIRMADO"

    def cambiar_estado(self, nuevo_estado: str) -> None:
        # Regla: solo hacia adelante y, para pasar a cocina, con pago confirmado.
        if nuevo_estado == "EN_PREPARACION" and self.estado_pago != "CONFIRMADO":
            raise ValueError("El pedido no puede ir a cocina sin pago confirmado")
        if ESTADOS.index(nuevo_estado) != ESTADOS.index(self.estado) + 1:
            raise ValueError(f"No se puede pasar de {self.estado} a {nuevo_estado}")
        self.estado = nuevo_estado
        self.historial.append(nuevo_estado)  # cada cambio deja una fila en el historial