*** Data Classes ***

from dataclasses import dataclass,  
from datetime import date
from typing import List

@dataclass
class Contribuyente:
    dni: int
    nombre: str


@dataclass
class Fallecido(Contribuyente):
    fecha_fallecimiento: date
    menor: bool
    

@dataclass
class Recibo:
    numero: int
    contribuyente: Contribuyente
    monto: float
    recargos: float


@dataclass
class Parcela:
    numero: int
    fila: int
    sector: str
    zona: str


@dataclass
class Pdi:
    fecha_registro: date
    oficina_registro: str
    departamento_registro: str
    fecha_presentacion: date
    fallecido: Fallecido
    dni_fallecido: int
    fecha_fallecimiento: date
    tramitante: str
    observaciones: str
    imagen_pdi: str


@dataclass
class Tasa:
    zona: str
    periodicidad: int
    monto: float
    fecha_desde: date
    fecha_hasta: date


@dataclass
class Usuario:
    usuario: str
    nombre: str
    password: str
    nivel_acceso: str


@dataclass
class Pago:
    fecha_pago: date
    recibo: Recibo
    fallecidos: List[Fallecido]
    reserva: bool
    contribuyente: Contribuyente
    parcela: Parcela
    fecha_vencimiento: date
    observacion_periodo: str
    observacion_anexa: str


