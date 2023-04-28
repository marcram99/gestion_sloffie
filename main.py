from fastapi import FastAPI, Request, Response, Depends
from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_pagination import add_pagination
from fastapi_pagination.links import Page
from fastapi_pagination.ext.sqlalchemy import paginate

from sqlalchemy.orm import Session
from sqlalchemy import select

from .database import SessionLocal, engine
from . import models, schema, crud

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

# -------------------------------------------------------------------------


@app.get("/user")
def get_users(request: Request, db: Session = Depends(get_db)) -> Page[schema.Client]:
    users: [schema.Client] = db.query(models.Client).all()
    return paginate(db, select(models.Client))
# --------------------------------------------------------------------------


@app.get("/clients")
async def read_all_client(request: Request,
                          db: Session = Depends(get_db)
                          ) -> Page[schema.Client]:
    results = paginate(db, select(models.Client))
    total = db.query(models.Client).count()
    print(f'DEBUG: {total=}')
    return templates.TemplateResponse("client.html",
                                      {"request": request,
                                       "results": results,
                                       "total": total
                                       }
                                      )


@app.post("/client")
async def create_user(client: schema.ClientCreate,
                      db: Session = Depends(get_db)
                      ):
    print(f'DEBUG:POST {client.nom=} {client.prenom=} ')
    return crud.create_client(db=db, client=client)


@app.put("/client/{client_id}")
async def update_user(client_id: int,
                      client: schema.ClientCreate,
                      db: Session = Depends(get_db)
                      ):
    print(f'DEBUG:PUT {client.nom=} {client.prenom=} ')
    return crud.update_client(db, client, client_id)


@app.delete("/client/{client_id}")
def delete_user(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_id(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        result = crud.delete_client(db, client_id)
    return result
