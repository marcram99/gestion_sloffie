from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static",
          StaticFiles(directory="gestion_sloffie/static"),
          name="static"
          )
templates = Jinja2Templates(directory="gestion_sloffie/templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("main.html",
                                      {"request": request,
                                       }
                                      )
