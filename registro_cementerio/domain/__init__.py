from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass(frozen=True)
class Name:
    name: str
    surname: str

@dataclass(frozen=True)
class Taxpayer:
    dni: int
    name: Name


@dataclass(frozen=True)
class Deceased(Taxpayer):
    death_date: date
    younger: bool
    

@dataclass(frozen=True)
class Receipt:
    receipt_number: int
    taxpayer: Taxpayer
    amount: float
    surcharge: float


@dataclass(frozen=True)
class Plot:
    plot_number: int
    row: int
    sector: str
    zone: str


@dataclass(frozen=True)
class Pdi:
    register_date: date
    register_office: str
    register_depto: str
    presentation_date: date
    deceased: Deceased
    presenter: Taxpayer
    observations: str
    pdi_image: str


@dataclass(frozen=True)
class Tax:
    zone: str
    periodicity: int
    amount: float
    date_from: date
    date_to: date


@dataclass(frozen=True)
class User:
    user: str
    user_name: Taxpayer
    password: str
    access_level: str


@dataclass(frozen=True)
class Payment:
    payment_date: date
    receipt: Receipt
    deceaseds: List[Deceased]
    reservation: bool
    taxpayer: Taxpayer
    plot: Plot
    due_date: date
    period_observation: str
    attached_observation: str


