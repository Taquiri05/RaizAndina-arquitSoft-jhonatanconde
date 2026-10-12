# =============================================================
# PRESENTACION · Rutas REST de pagos (Flask)
# =============================================================
# La ruta solo traduce HTTP <-> caso de uso. No contiene reglas
# del negocio ni sabe qué pasarela se usa.
# (Este archivo necesita Flask; demo.py funciona sin él.)

from flask import Blueprint, jsonify, request

from aplicacion.servicio_de_pagos import ServicioDePagos


def crear_rutas_de_pagos(servicio: ServicioDePagos, buscar_pedido) -> Blueprint:
    rutas = Blueprint("pagos", __name__)

    @rutas.post("/api/pedidos/<int:pedido_id>/pagos")
    def pagar(pedido_id: int):
        referencia = servicio.pagar(buscar_pedido(pedido_id))
        return jsonify({"referencia": referencia}), 201

    @rutas.post("/api/webhooks/pagos")
    def recibir_aviso():
        datos = request.get_json()
        pedido = buscar_pedido(datos["pedido_id"])
        procesado = servicio.confirmar_pago(pedido, datos["id_evento"], datos["referencia"])
        return jsonify({"procesado": procesado}), 200

    return rutas