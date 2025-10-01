from fastapi import FastAPI
from .database import db 
from .database import crud 
from app import models 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pathlib import Path


app = FastAPI()

db.init_db()

templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

@app.get("/", response_class=HTMLResponse)
def front_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/criar_produto/")
def criar_produto(nome: str, quantidade: int):
    return crud.add_produto(nome, quantidade)

@app.get("/listar_produtos/")
def listar_todos_produtos():
    return crud.listar_produtos()

@app.get('/excluir_produto/{id}')
def excluir_produto(id: int):
    return crud.excluir_produto(id=id)

@app.get('/editar_produto/{id}/{quantidade}')
def excluir_produto(id: int, quantidade: int):
    return crud.editar_quantidade(id=id, quantidade=quantidade)