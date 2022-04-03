from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import roteadores

app = FastAPI()

templates = Jinja2Templates ( directory="templates" )
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get ("/", response_class=HTMLResponse )
async def index(request: Request) :
    return templates.TemplateResponse ("index.html", {"request" : request } )


@app.get ("/lista", response_class=HTMLResponse )
async def index(request: Request):
    lista = roteadores.Roteadores()
    return templates.TemplateResponse ("lista.html", {"request" : request, 'exibirlista': lista})


if __name__ == '__mail__':
    app.rum(debug=True)
