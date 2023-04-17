from fastapi import FastAPI, Request, Response, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, schema, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
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


@app.post("/new_client")
async def create_client(client: schema.ClientCreate, 
                        db: Session = Depends(get_db)
                        ):
    return crud.create_client(db=db, client=client)


@app.get("/clients")
async def read_all_client(request: Request, db: Session = Depends(get_db)):
    results = db.query(models.Client).all()
    for elem in results:
        print(f'{elem.nom=} {elem.prenom=}')
    print("retour de query")
    return templates.TemplateResponse("client.html",
                                      {"request": request,
                                       "results": results,
                                       }
                                      )
