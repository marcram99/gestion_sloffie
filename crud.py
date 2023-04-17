from sqlalchemy import update
from sqlalchemy.orm import Session

from . import models, schema


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: schema.ClientCreate):
    print(f'DEBUG:crud-create_client: {client=}')
    db_client = models.Client(nom=client.nom,
                              prenom=client.prenom,
                              no_tel=client.no_tel,
                              mail=client.mail)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client
