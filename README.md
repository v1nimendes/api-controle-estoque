# Sistema de Gerenciamento de Estoque

##  Visão Geral

Este projeto é um sistema de gerenciamento de estoque (CRUD) desenvolvido como parte de um estudo prático sobre a construção de APIs web com Python. A aplicação permite criar, listar, editar e excluir produtos, utilizando uma interface web para interagir com o backend.

O principal objetivo foi aplicar e solidificar conhecimentos em desenvolvimento backend com **FastAPI**, manipulação de banco de dados e a criação de uma interface frontend para consumir a API.

##  Interface da Aplicação

A interface web permite que o usuário realize todas as operações de forma intuitiva.

![Tela principal da aplicação com a lista de produtos e os formulários de ações.](https://github.com/v1nimendes/api-controle-estoque/blob/main/img/tela.png?raw=true)
*Visão geral da aplicação.*

##  Arquitetura do Projeto

A estrutura do código foi organizada em módulos para promover a **Separação de Responsabilidades**, o que melhora a clareza e a manutenibilidade do projeto:

* **`main.py` (Camada de Apresentação)**: Define as rotas da API, recebe as requisições HTTP e retorna as respostas. É o ponto de entrada da aplicação.
* **`crud.py` (Camada de Lógica de Negócio)**: Contém toda a lógica de manipulação dos dados. As funções neste módulo são responsáveis por interagir com o banco de dados para executar as operações CRUD (`add_produto`, `listar_produtos`, etc.).
* **`db.py` (Camada de Acesso a Dados)**: Gerencia a conexão e a inicialização do banco de dados SQLite, fornecendo uma conexão quando necessário.
* **`models.py` (Camada de Modelos)**: Define os esquemas de dados (schemas) com Pydantic, garantindo que os dados que entram na aplicação tenham o formato correto.

Além disso, a comunicação entre o frontend e o backend segue os princípios de uma **API RESTful**, e o código inclui **Tratamento de Erros** com `HTTPException` para fornecer feedback claro ao cliente.

## 🛠️ Tecnologias Utilizadas

* **Backend**:
    * Python 3
    * FastAPI
    * Pydantic
    * SQLite 3

* **Frontend**:
    * HTML5
    * CSS3
    * JavaScript
    * Jinja2Templates

##  Como Executar

Para rodar este projeto localmente, você precisará ter o Python instalado e seguir estes passos:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/v1nimendes/api-controle-estoque.git](https://github.com/v1nimendes/api-controle-estoque.git)
    cd api-controle-estoque
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install fastapi uvicorn "jinja2[async]"
    ```

4.  **Execute a aplicação:**
    ```bash
    fastapi dev main.py 
    ```

5.  Abra seu navegador e acesse `http://127.0.0.1:8000` para interagir com a aplicação.
