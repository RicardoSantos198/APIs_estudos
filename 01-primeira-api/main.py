from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    nome: str
    preco: float

produtos = [
        {"id":1, "nome":"Pizza de calabresa",
         "preco": 45.00},
         {"id": 2, "nome": "Pizza de queijo", "preco":40.00},
         {"id": 3, "nome": "Pizza de frango", "preco": 42.00}
]

@app.get("/")
def inicio():
    return {"mensagem": "Minha primeira API está funcionando"}

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{id}")
def buscar_produto(id:int):

    for produto_atual in produtos:
        if produto_atual["id"] == id:
            return produto_atual

    return{"mensagem": "Produto não encontrado..."}


@app.post("/produtos")
def criar_produto(produto: Produto):
    novo_produto = produto.model_dump()
    novo_produto["id"]= len(produtos) + 1

    produtos.append(novo_produto)

    return novo_produto


@app.put("/produtos/{id}")
def atualizar_produto(id:int, produto: Produto):
    for produto_atual in produtos:
        if produto_atual["id"] == id:

            produto_atual.update(produto.model_dump())
    
            return produto_atual

    return{"mensagem": "Produto não encontrado"}


@app.delete("/produtos/{id}") 
def deletar_produto(id:int):
    for produto_atual in produtos:
        if produto_atual ["id"] == id:

         produtos.remove(produto_atual)

         return{"mensagem": "Produto excluído com sucesso"}
    
    return{"mensagem:" "Produto não encontrado"}


