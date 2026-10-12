# =============================================================
# INFRAESTRUCTURA · Adaptador de Mercado Pago (simulado)
# =============================================================
# Cumple el contrato PasarelaDePago. Es SIMULADO: no se conecta
# a internet. Aquí iría la llamada real al proveedor y la
# traducción de sus estados al vocabulario del sistema.

from dominio.pasarela_de_pago import PasarelaDePago, ResultadoCobro


class AdaptadorMercadoPagoSimulado(PasarelaDePago):
    def __init__(self):
        self.pagos: dict[str, str] = {}

    def cobrar(self, monto: float, correo: str, clave_unica: str) -> ResultadoCobro:
        referencia = f"MP-{clave_unica}"
        self.pagos[referencia] = "approved"  # estado en el idioma del proveedor
        print(f"[Mercado Pago simulado] cobro de S/ {monto:.2f} a {correo}")
        return ResultadoCobro(referencia, "pendiente")

    def consultar_pago(self, referencia: str) -> ResultadoCobro:
        # Traduce "approved" / "rejected" a "aprobado" / "fallido".
        traduccion = {"approved": "aprobado", "rejected": "fallido"}
        estado = traduccion.get(self.pagos.get(referencia, ""), "pendiente")
        return ResultadoCobro(referencia, estado)