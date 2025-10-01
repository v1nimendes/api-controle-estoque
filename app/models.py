from pydantic import BaseModel

class criarProduto(BaseModel):
    nome: str
    quantidade: int