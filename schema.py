from typing import List, Optional
from pydantic import BaseModel


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


class FactureBase(BaseModel):
    timestamp: str
    produit: str
    remise: str
    prix: str
   

class FactureCreate(BaseModel):
    pass


class Facture(BaseModel):
    id: int
    client_id: int

    class Config:
        orm_mode = True
   

class ClientBase(BaseModel):
    nom: str
    prenom: str
    date_naissance: Optional[str] = None
    adresse: Optional[str] = None
    code_postal: Optional[int] = None
    ville: Optional[str] = None
    no_tel: str
    mail: str


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int
    agenda: List[Cours] = []

    class Config:
        orm_mode = True
