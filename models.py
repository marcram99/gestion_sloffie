from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    date_naissance = Column(String)
    adresse = Column(String)
    code_postal = Column(String)
    no_tel = Column(String)
    mail = Column(String)

    agenda = relationship("Cours", back_populates="owner")


class Cours(Base):
    __tablename__ = "cours"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    formule = Column(String)
    paye = Column(Boolean)

    owner = relationship("Client", back_populates="agenda")
