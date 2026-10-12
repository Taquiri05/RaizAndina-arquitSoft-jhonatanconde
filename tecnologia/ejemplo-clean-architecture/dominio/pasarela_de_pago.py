# =============================================================
# DOMINIO · Contrato PasarelaDePago
# =============================================================
# Observe el vocabulario: "cobrar", "consultar_pago". No dice
# Mercado Pago. Habla el idioma del negocio, no el del proveedor;
# por eso se puede cambiar de proveedor sin tocar este archivo (ADR-004).

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ResultadoCobro:
    referencia: str
    estado: str  # "aprobado", "pendiente" o "fallido"


class PasarelaDePago(ABC):
    @abstractmethod
    def cobrar(self, monto: float, correo: str, clave_unica: str) -> ResultadoCobro:
        """Crea el cobro. La clave única evita cobrar dos veces si se reintenta."""

    @abstractmethod
    def consultar_pago(self, referencia: str) -> ResultadoCobro:
        """Pregunta al proveedor el estado real del pago."""