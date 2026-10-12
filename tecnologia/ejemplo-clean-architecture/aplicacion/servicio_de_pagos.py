# =============================================================
# APLICACION · Caso de uso ServicioDePagos
# =============================================================
# Coordina el pago: cobrar -> recibir aviso -> verificar -> confirmar.
# No contiene reglas del pedido (se las pide a la entidad) y no
# conoce ningún proveedor: habla solo con el contrato PasarelaDePago.

from dominio.pasarela_de_pago import PasarelaDePago
from dominio.pedido import Pedido


class ServicioDePagos:
    def __init__(self, pasarela: PasarelaDePago):
        # La pasarela se recibe desde afuera (inversión de dependencias).
        self.pasarela = pasarela
        self.eventos_procesados: set[str] = set()  # papel de WebhookEvento (ADR-006)

    def pagar(self, pedido: Pedido) -> str:
        # El monto y el correo los define el servidor, no el cliente.
        resultado = self.pasarela.cobrar(
            monto=pedido.total(),
            correo=pedido.correo_cliente,
            clave_unica=f"pedido-{pedido.id}",
        )
        return resultado.referencia

    def confirmar_pago(self, pedido: Pedido, id_evento: str, referencia: str) -> bool:
        # 1. Si el aviso ya se procesó, no se procesa de nuevo.
        if id_evento in self.eventos_procesados:
            return False
        self.eventos_procesados.add(id_evento)

        # 2. Se consulta al proveedor para comprobar que el aviso es auténtico.
        if self.pasarela.consultar_pago(referencia).estado != "aprobado":
            return False

        # 3. Pago confirmado: el pedido queda listo para la cocina.
        pedido.confirmar_pago()
        pedido.cambiar_estado("EN_PREPARACION")
        return True