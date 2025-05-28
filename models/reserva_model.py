from flask import jsonify
from config import db

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
