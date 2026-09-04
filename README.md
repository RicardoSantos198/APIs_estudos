<h1>🍕 Primeira API — CRUD de Produtos</h1>

<h4>Minha primeira API REST, desenvolvida como prática após o curso de **Node.js, API REST e MongoDB** da Alura. O curso foi ótimo, mas bastante conceitual — este projeto foi o jeito que encontrei de sair da teoria e realmente aplicar os conceitos na prática, construindo uma API do zero.</h4>

Levei cerca de **4 horas** para desenvolver(deu um trabalho! 😅😅).

<h3>💡 Sobre o projeto</h3>

Uma API simples de CRUD (Create, Read, Update, Delete) para gerenciar um catálogo de produtos. No caso, um cardápio de pizzas. O objetivo era entender na prática como funcionam:

- Rotas HTTP (GET, POST, PUT, DELETE)
- Path parameters (`/produtos/{id}`)
- Validação de dados de entrada com Pydantic
- Manipulação de uma "base de dados" em memória (lista de dicionários)

<h3> 🛠️ Tecnologias utilizadas</h3>

- **[FastAPI](https://fastapi.tiangolo.com/)** — framework Python usado como servidor para criar e testar a API
- **[Pydantic](https://docs.pydantic.dev/)** — validação e modelagem dos dados recebidos nas requisições
- **Python 3.11**
- **Uvicorn** (servidor ASGI, instalado como dependência do FastAPI) para rodar a aplicação localmente

<h3>📋 Endpoints</h3>

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/` | Mensagem de boas-vindas, confirma que a API está no ar |
| `GET` | `/produtos` | Lista todos os produtos cadastrados |
| `GET` | `/produtos/{id}` | Busca um produto específico pelo ID |
| `POST` | `/produtos` | Cria um novo produto |
| `PUT` | `/produtos/{id}` | Atualiza um produto existente |
| `DELETE` | `/produtos/{id}` | Remove um produto |

### Modelo de dados (`Produto`)

```json
{
  "nome": "Pizza de calabresa",
  "preco": 45.00
}
```

> Os dados são armazenados apenas em memória (uma lista Python), então tudo é resetado sempre que o servidor é reiniciado. Não há um banco de dados real — o foco aqui era entender a lógica das rotas.

<h3>## 🚀 Como rodar o projeto</h3>

1. Clone o repositório e entre na pasta `01-primeira-api`

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install fastapi "uvicorn[standard]"
   ```

4. Rode o servidor:
   ```bash
   fastapi dev main.py
   ```
   ou
   ```bash
   uvicorn main:app --reload
   ```

5. A API estará disponível em `http://127.0.0.1:8000`

6. A documentação interativa (gerada automaticamente pelo FastAPI) fica em:
   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

<h3>🧪 Testando a API</h3>

O arquivo [`teste.http`](./teste.http) contém exemplos prontos de todas as requisições (GET, POST, PUT, DELETE). Se você usa VS Code, a extensão **REST Client** permite executar essas requisições direto do editor, sem precisar do Postman ou Insomnia.

<h3>## 📚 Aprendizados</h3>

- Como estruturar rotas RESTful com FastAPI
- Diferença prática entre os métodos HTTP e quando usar cada um
- Validação automática de dados de entrada com Pydantic (`BaseModel`)
- Como o FastAPI gera documentação interativa automaticamente a partir do código
- Manipulação de listas/dicionários em Python como uma "base de dados" simples

---

Projeto feito para fins de estudo, parte da série [`APIs_estudos`](../).
