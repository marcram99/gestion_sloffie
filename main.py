from fastapi import FastAPI, Request, Response, Depends
from fastapi import HTTPException
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
    return templates.TemplateResponse("client.html",
                                      {"request": request,
                                       "results": results,
                                       }
                                      )


@app.post("/api/users")
async def create_user(client: schema.ClientCreate,
                      db: Session = Depends(get_db)
                      ):
    print(f'DEBUG:POST {client.nom=} {client.prenom=} ')
    return crud.create_client(db=db, client=client)


@app.put("/api/users/{client_id}")
async def update_user(client_id: int,
                      client: schema.ClientCreate,
                      db: Session = Depends(get_db)
                      ):
    print(f'DEBUG:PUT {client.nom=} {client.prenom=} ')
    return crud.update_client(db, client, client_id)


@app.delete("/api/users/{client_id}")
def delete_user(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        result = crud.delete_client(db, client_id)
    return result
