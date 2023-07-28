from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel


class FactureBase(BaseModel):
    date_facture: Optional[str]
    #timestamp: Optional[datetime] 
    produit:Optional[str] = None
    remise: Optional[str] = None
    prix: Optional[str] = None
    user_id: int


class FactureCreate(FactureBase):
    pass


class Facture(FactureBase):
    id: int

    class Config:
        orm_mode = True

class CoursBase(BaseModel):
    timestamp: str
    formule: str
    paye: bool


class CoursCreate(CoursBase):
    pass


class Cours(CoursBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True



class ClientBase(BaseModel):
    nom: str
    prenom: str
    date_naissance: Optional[str] = None
    adresse: Optional[str] = None
    code_postal: Optional[str] = None
    ville: Optional[str] = None
    no_tel: Optional[str] = None
    mail: Optional[str] = None


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int
    agenda: List[Cours] = []
    bill: List[Facture] = []

    class Config:
        orm_mode = True



