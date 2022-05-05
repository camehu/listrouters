from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import roteador

app = FastAPI()

templates = Jinja2Templates( directory="templates" )


@app.get ( "/", response_class=HTMLResponse)
async def index(request: Request):
    lista = roteador.paginas
    return templates.TemplateResponse( "index.html", {"request" : request, 'lista': lista} )


if __name__ == '__mail__':
    app.rum()
