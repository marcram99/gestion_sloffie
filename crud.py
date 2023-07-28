from sqlalchemy import update
from sqlalchemy.orm import Session

from . import models, schema


def get_client_by_id(db: Session, id: int):
    print(f'DEBUG_CRUD:get_client_by_id : {id}')
    db_request =  db.query(models.Client).filter(models.Client.id == id).first()
    return db.query(models.Client).filter(models.Client.id == id).first()


def get_all_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schema.ClientCreate):
    print(f'DEBUG_CRUD:create_client: {client=}')
    db_client = models.Client(nom=client.nom,
                              prenom=client.prenom,
                              no_tel=client.no_tel,
                              mail=client.mail,
                              adresse=client.adresse,
                              ville=client.ville,
                              code_postal=client.code_postal)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def update_client(db: Session, modif: schema.ClientCreate, client_id: int):
    db_client = db.query(models.Client).filter(models.Client.id == client_id).first()
    db_client.nom = modif.nom
    db_client.prenom = modif.prenom
    db_client.adresse = modif.adresse
    db_client.code_postal = modif.code_postal
    db_client.ville = modif.ville
    db_client.mail = modif.mail
    db_client.no_tel = modif.no_tel
    db.commit()
    return {"update": "finished"}


def delete_client(db: Session, client_id: int):
    rec = db.query(models.Client).filter(models.Client.id == client_id).first()
    db.delete(rec)
    db.commit()
    return {"action": "user_deleted"}


def create_facture(db: Session, facture: schema.Facture):
    print(f'DEBUG_CRUD:create_facture: {facture=}')
    db_facture = models.Facture(
                                #timestamp=facture.timestamp,
                                fact_date=facture.date_facture,
                                timestamp=facture.date_facture,
                                produit=facture.produit,
                                prix=facture.prix,
                                user_id=facture.user_id
                                )
    db.add(db_facture)
    db.commit()
    db.refresh(db_facture)
    return db_facture

def get_facture_by_id(db: Session, fact_id: int):
    print(f'DEBUG_CRUD:get_facture_by_id: {fact_id=}')
    rec = db.query(models.Facture).filter(models.Facture.id == fact_id).first()
    return rec


def delete_facture(db: Session, fact_id: int):
    print(f'DEBUG_CRUD:del_facture: {fact_id=}')
    rec = db.query(models.Facture).filter(models.Facture.id == fact_id).first()
    db.delete(rec)
    db.commit()
    return {"action": "facture_deleted"}
