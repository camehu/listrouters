from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates ( directory="templates" )


@app.get ("/", response_class=HTMLResponse )
async def index(request: Request) :
    return templates.TemplateResponse ("index.html", {"request" : request} )


if __name__ == '__mail__':
    app.rum(debug=True)
