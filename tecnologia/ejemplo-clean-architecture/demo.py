# =============================================================
# DEMO · Ensambla las capas y recorre el flujo pedido -> pago -> cocina
# =============================================================
# Ejecutar con:  python demo.py   (no necesita base de datos ni internet)
# Solo aquí se decide qué adaptador se usa: cambiar de proveedor
# es cambiar UNA línea.

from aplicacion.servicio_de_pagos import ServicioDePagos
from dominio.pedido import DetallePedido, Pedido
from infraestructura.adaptador_mercado_pago_simulado import AdaptadorMercadoPagoSimulado
from infraestructura.adaptador_otra_pasarela_simulado import AdaptadorOtraPasarelaSimulado


def recorrer_flujo(servicio: ServicioDePagos) -> None:
    pedido = Pedido(
        id=1, sede_id=1, correo_cliente="cliente@correo.com",
        detalles=[DetallePedido("Puca picante", 18.0, 2), DetallePedido("Chicha morada", 6.0, 1)],
    )
    referencia = servicio.pagar(pedido)
    print("Primer aviso procesado:", servicio.confirmar_pago(pedido, "evento-1", referencia))
    print("Aviso repetido procesado:", servicio.confirmar_pago(pedido, "evento-1", referencia))
    pedido.cambiar_estado("LISTO")
    print("Historial del pedido:", " -> ".join(pedido.historial))


print("=== Con Mercado Pago ===")
recorrer_flujo(ServicioDePagos(AdaptadorMercadoPagoSimulado()))

print("\n=== Cambiando de proveedor (sin tocar dominio ni caso de uso) ===")
recorrer_flujo(ServicioDePagos(AdaptadorOtraPasarelaSimulado()))