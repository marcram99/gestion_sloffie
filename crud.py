from sqlalchemy import update
from sqlalchemy.orm import Session

from . import models, schema


def get_client(db: Session, client_id: int):
    print(f'DEBUG: crud_get_user: id = {client_id}')
    return db.query(models.Client).filter(models.Client.id == client_id).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schema.ClientCreate):
    print(f'DEBUG:crud-create_client: {client=}')
    db_client = models.Client(nom=client.nom,
                              prenom=client.prenom,
                              no_tel=client.no_tel,
                              mail=client.mail,
                              adresse=client.adresse,
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
    db_client.mail = modif.mail
    db_client.no_tel = modif.no_tel
    db.commit()
    return {"update": "finished"}


def delete_client(db: Session, client_id: int):
    rec = db.query(models.Client).filter(models.Client.id == client_id).first()
    db.delete(rec)
    db.commit()
    return {"action": "user_deleted"}
