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
    ville = Column(String)
    no_tel = Column(String)
    mail = Column(String)

    bill = relationship("Facture", back_populates="user")


class Facture(Base):
    __tablename__ = "facture"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String)
    date_fact = Column(String)
    produit = Column(String)
    prix = Column(String)
    remise = Column(String)
    user_id = Column(Integer, ForeignKey("client.id"))

    user = relationship("Client", back_populates="bill")
