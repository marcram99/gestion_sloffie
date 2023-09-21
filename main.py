from fastapi import FastAPI, Request, Response, Depends
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_pagination import add_pagination
from fastapi_pagination.links import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import select

from .database import SessionLocal, engine
from . import models, schema, crud
from . import new_pdf

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
add_pagination(app)
app.mount("/static",
          StaticFiles(directory="gestion_sloffie/static"),
          name="static"
          )
templates = Jinja2Templates(directory="gestion_sloffie/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("main.html",
                                      {"request": request,
                                       }
                                      )


@app.get("/clients")
async def read_all_client(request: Request,
                          db: Session = Depends(get_db)
                          ) -> Page[schema.Client]:
    results = paginate(db, select(models.Client).order_by(models.Client.nom))
    return templates.TemplateResponse("client.html",
                                      {"request": request,
                                       "results": results,
                                       })


@app.post("/client")
async def create_user(client: schema.ClientCreate,
                      db: Session = Depends(get_db)
                      ):
    print(f'DEBUG_MAIN:Cree user {client.nom=} {client.ville=} ')
    return crud.create_client(db=db, client=client)


@app.post("/client/{client_id}")
async def info_user(client_id: int,
                    db: Session = Depends(get_db)
                    ) -> schema.Client:
    print(f'DEBUG_MAIN: {client_id=} ')
    result = crud.get_client_by_id(db, client_id)
    print(f'DEBUG_MAIN_found: {result} ')
    print(f'DEBUG_MAIN_found: {type(result)=} ')
    return result


@app.put("/client/{client_id}")
async def update_user(client_id: int,
                      client: schema.ClientCreate,
                      db: Session = Depends(get_db)
                      ):
    print(f'DEBUG_MAIN:PUT {client.nom=} {client.prenom=} ')
    return crud.update_client(db, client, client_id)


@app.delete("/client/{client_id}")
async def delete_user(client_id: int,
                db: Session = Depends(get_db)):
    db_client = crud.get_client_by_id(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        result = crud.delete_client(db, client_id)
    return result

@app.get("/catalogue")
async def catalogue(request:Request):
    return templates.TemplateResponse("catalogue.html",
                                      {"request":request,
                                       })
@app.get("/factures")
async def read_all_facture(request: Request,
                           db: Session = Depends(get_db)
                           ) -> Page[schema.Facture]:
    resultat = paginate(db, select(models.Facture).order_by(models.Facture.timestamp))
    return templates.TemplateResponse("facture.html",
                                      {"request": request,
                                       "results": resultat,
                                       "mode": "all",
                                       }
                                      )


@app.get("/factures/{client_id}")
async def read_client_facture(client_id: int,
                              request: Request,
                              db: Session = Depends(get_db)
                              ) -> Page[schema.Facture]:
    facture_info = paginate(db, select(models.Facture).filter(models.Facture.user_id == client_id).order_by(models.Facture.timestamp))
    client_info = crud.get_client_by_id(db, client_id)
    return templates.TemplateResponse("facture.html",
                                      {"request": request,
                                       "results": facture_info,
                                       "mode": "client",
                                       "info_client": client_info,
                                       }
                                      )
 

@app.post("/factures/{client_id}") 
async def new_facture(client_id: int,
                      data: schema.FactureCreate,
                      db: Session = Depends(get_db)
                      ):
    client = crud.get_client_by_id(db, client_id)
    print(f'new facture for no: {client.prenom} {client.nom}')
    print(f'new facture: {data.produit=}')
    #data.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill = crud.create_facture(db, facture=data)
    return bill


@app.post("/facture/{fact_id}") 
async def new_facture(fact_id: int,
                      db: Session = Depends(get_db)
                      ):
    facture = crud.get_facture_by_id(db, fact_id)
    print(f'read facture: {facture.id=}')
    return facture


@app.put("/facture/{fact_id}") 
async def update_facture(fact_id: int,
                         data: schema.FactureCreate,
                         db: Session = Depends(get_db)
                         ):
    facture = crud.update_facture(db, data, fact_id)
    print(f'update facture: {facture.id=}')
    return facture

@app.delete("/facture/{fact_id}")
async def delete_facture(fact_id: int,
                         db: Session = Depends(get_db)
                         ):
    result = crud.delete_facture(db, fact_id)
    return result


@app.post("/generate_pdf/{client_id}/{fact_id}")
async def pdf_facture(client_id: int,
                      fact_id: str,
                      db: Session = Depends(get_db),
                      ): 
    client = crud.get_client_by_id(db, client_id)
    facture = crud.get_facture_by_id(db, fact_id)
    print(f"DEBUG_MAIN-PDF: {fact_id=}")
    print(f'PDF for {client.nom} {client.prenom}/{facture.produit}')
    #facture_pdf.generate_pdf(client, facture)
    new_pdf.generate_pdf(client, facture)
