from utils.ma import ma
from models.persona import Persona
from schemas.ubigeo_schema import UbigeoSchema

class PersonaSchema(ma.Schema):
    class Meta:
        model = Persona
        fields = (
            'documento',
            'tipo_documento',
            'id_ubigeo',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'sexo',
            'telefono',
            'ubigeo'
        )
        
    ubigeo = ma.Nested(UbigeoSchema)
    
persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)