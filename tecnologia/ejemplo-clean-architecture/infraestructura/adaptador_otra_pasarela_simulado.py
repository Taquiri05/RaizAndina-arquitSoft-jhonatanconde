# =============================================================
# INFRAESTRUCTURA · Otra pasarela (simulada)
# =============================================================
# Mismo contrato, otro proveedor. Sirve para demostrar que
# cambiar de pasarela no obliga a tocar el dominio ni el caso de uso.

from dominio.pasarela_de_pago import PasarelaDePago, ResultadoCobro


class AdaptadorOtraPasarelaSimulado(PasarelaDePago):
    def cobrar(self, monto: float, correo: str, clave_unica: str) -> ResultadoCobro:
        print(f"[Otra pasarela simulada] cobro de S/ {monto:.2f} a {correo}")
        return ResultadoCobro(f"OTRA-{clave_unica}", "pendiente")

    def consultar_pago(self, referencia: str) -> ResultadoCobro:
        return ResultadoCobro(referencia, "aprobado")