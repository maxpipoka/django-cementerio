*** Data Classes ***

from dataclasses importdataclass,  
from datetime import date

@dataclass
class Persona:
    dni: int
    nombre: str

@dataclass
class Contribuyente(Persona):
    