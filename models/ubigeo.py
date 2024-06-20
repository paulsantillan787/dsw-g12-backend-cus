from utils.db import db
from dataclasses import dataclass

@dataclass
class Ubigeo(db.Model):
    __tablename__ = 'ubigeo'
    
    id_ubigeo = db.Column(db.String(6), primary_key=True)
    departamento = db.Column(db.String(60))
    provincia = db.Column(db.String(60))
    distrito = db.Column(db.String(60))
    
    persona = db.relationship('Persona', backref='ubigeo', cascade='all, delete-orphan')
    
    def __init__(self, id_ubigeo, departamento, provincia, distrito):
        self.id_ubigeo = id_ubigeo
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito