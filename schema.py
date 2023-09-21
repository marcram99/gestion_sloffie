from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel


class FactureBase(BaseModel):
    timestamp: str 
    produit :str 
    prix: Optional[str] = None
    remise: Optional[str] = None
    user_id: int


class FactureCreate(FactureBase):
    pass


class Facture(FactureBase):
    id: int

    class Config:
        from_attributes=True


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
    bill: List[Facture] = []

    class Config:
        from_attributes=True
        #orm_mode = True
