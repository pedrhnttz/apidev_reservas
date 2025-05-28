from flask import Blueprint, request, jsonify

from models.reserva_model import get_reservas, get_reserva_by_id, create_reserva, update_reserva, delete_reserva

reservas_bp = Blueprint('reservas', __name__)

@reservas_bp.route("/reservas", methods=["GET"])
def getReservas():
    return jsonify(get_reservas())

@reservas_bp.route("/reservas/<int:id>", methods=["GET"])
def getReservaById(id):
    try:
        reserva = get_reserva_by_id(id)
        return jsonify(reserva), 200
    except Exception as e:
        return jsonify({'erro': str(e)})
    
@reservas_bp.route('/reservas', methods=['POST'])
def createReserva():
    try:
        data = request.json
        reserva = create_reserva(data)
        return jsonify(reserva)
    except Exception as e:
        return jsonify({'erro': str(e)})
