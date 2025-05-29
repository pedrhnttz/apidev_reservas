from config import db
from flask import jsonify
from datetime import date, datetime
import requests

main_api = "http://127.0.0.1:5000/api"

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(20), nullable=False)
    hora_inicio = db.Column(db.String(10), nullable=False)
    hora_fim = db.Column(db.String(10), nullable=False)

    def __init__(self, turma_id, sala, data, hora_inicio, hora_fim):
        self.turma_id = turma_id
        self.sala = sala
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim =  hora_fim

    def to_dict(self):
        return {
            "id":self.id,
            "turma_id":self.turma_id,
            "sala":self.sala,
            "data":self.data,
            "hora_inicio":self.hora_inicio,
            "hora_fim":self.hora_fim
        }
    
# Classes de exceção

class ReservaNotFound(Exception):
    def __init__(self):
        super().__init__({'Reserva não encontrada'})

# Funções de rota

def get_reservas():
    reservas = Reserva.query.all()
    return [r.to_dict() for r in reservas]

def get_reserva_by_id(id):
    reserva = Reserva.query.get(id)
    if not reserva:
        raise ReservaNotFound
    return reserva.to_dict()

def create_reserva(reserva):
    is_valid, error_msg = validar_reserva(reserva)
    if not is_valid:
        return jsonify({'erro': error_msg}), 400
    
    reserva_data = reserva.get('data')
    data_obj = datetime.strptime(reserva_data, "%Y-%m-%d").date()

    is_overlap_free, overlap_error_msg = validar_overlap(
            reserva_data.get('sala'),
            data_obj, # Passa o objeto date já convertido
            reserva_data.get('hora_inicio'),
            reserva_data.get('hora_fim')
        )
    if not is_overlap_free:
            return None, overlap_error_msg

    nova_reserva = Reserva(
        turma_id = reserva.get('turma_id'),
        sala = reserva.get('sala'),
        data = data_obj,
        hora_inicio = reserva.get('hora_inicio'),
        hora_fim = reserva.get('hora_fim')
    )

    db.session.add(nova_reserva)
    db.session.commit()
    return nova_reserva, None

def update_reserva():
    pass

def delete_reserva():
    pass

# Funções secundárias

def validar_reserva(dados):
    required_fields = {
        "turma_id": "ID da turma",
        "sala": "Sala",
        "data": "Data",
        "hora_inicio": "Horário de início",
        "hora_fim": "Horário de término"
    }

    for field, display_name in required_fields.items():
        if field not in dados or not dados[field]:
            return False, f"O campo '{display_name}' é obrigatório."
        
    turma_id = dados.get('turma_id')
    if not validar_turma(turma_id):
        return False, f'Turma não encontrada.'
    
    data_reserva = dados.get('data')
    if not validar_data(data_reserva):
        return False, "O campo 'Data' possui um formato inválido. Use AAAA-MM-DD."
    
    hora_inicio = dados.get('hora_inicio')
    hora_fim = dados.get('hora_fim')
    is_horas_valid, horas_error_msg = validar_hora(hora_inicio, hora_fim)
    if not is_horas_valid:
        return False, horas_error_msg
    
    return True, None

def validar_turma(turma_id):
    try:
        r = requests.get(f"{main_api}/turmas/{turma_id}")
        return r.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def validar_data(data_str, formato="%Y-%m-%d"):
    try:
        datetime.strptime(data_str, formato)
        return True
    except ValueError:
        return False

def validar_hora(hora_inicio, hora_fim, formato="%H:%M"):
    try:
        dt_hora_inicio = datetime.strptime(hora_inicio, formato).time()
        dt_hora_fim = datetime.strptime(hora_fim, formato).time()
    except ValueError:
        return False, f"O formato das horas deve ser '{formato}' (ex: 09:00)."
    if dt_hora_inicio >= dt_hora_fim:
        return False, "A 'Hora de início' deve ser anterior à 'Hora de término'."
    return True, None

def validar_overlap(sala, data_reserva_obj, hora_inicio_str, hora_fim_str):
    nova_hora_inicio = datetime.strptime(hora_inicio_str, "%H:%M").time()
    nova_hora_fim = datetime.strptime(hora_fim_str, "%H:%M").time()

    existing_reservas = db.session.query(Reserva).filter(
        Reserva.sala == sala,
        Reserva.data == data_reserva_obj
    ).all()

    for existing_reserva in existing_reservas:
        existente_hora_inicio = datetime.strptime(existing_reserva.hora_inicio, "%H:%M").time()
        existente_hora_fim = datetime.strptime(existing_reserva.hora_fim, "%H:%M").time()
        if (nova_hora_inicio < existente_hora_fim) and \
           (nova_hora_fim > existente_hora_inicio):
            return False, f"A sala '{sala}' já está reservada das {existing_reserva.hora_inicio} às {existing_reserva.hora_fim} nesta data."

    return True, None
