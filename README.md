Introdução
A Gourmet Express API é uma interface RESTful que fornece uma lista de receitas de diferentes pratos. A API é construída usando o FastAPI e permite que os usuários acessem informações sobre vários alimentos, incluindo ingredientes, autor e tempo de preparação.
Estrutura da API
• URL base : http://localhost:8000(para uso local)
Pontos finais
1. Ponto de extremidade raiz
• URL :/
• Método :GET
• Descrição : Retorna uma mensagem de boas-vindas.
Exemplo de Requisição
http
Copiar código
GET / HTTP/1.1
Host: localhost:8000
Exemplo de Resposta
json
Copiar código
{
    "mensagem": "Hello welcome to gourmet express."
}
 
2. Listar Alimentos
• URL :/foods
• Método :GET
• Descrição : Retorna uma lista de alimentos disponíveis na base de dados.
Exemplo de Requisição
http
Copiar código
GET /foods HTTP/1.1
Host: localhost:8000
Exemplo de Resposta
json
Copiar código
[
    {
        "name": "Spaghetti Bolognese",
        "author": "Carlos Christian",
        "recipe": "Cozinhe o espaguete com molho bolonhesa",
        "preparation_time": 30
    },
    {
        "name": "Feijoada",
        "author": "Ana Maria",
        "recipe": "Feijão preto com carne de porco e linguiça",
        "preparation_time": 120
    },
    ...
]
Estrutura do ObjetoFood
Cada objeto Foodpossui as seguintes propriedades:
• nome (string): Nome do prato.
• autor (string): Autor da receita.
• receita (string): Instruções para preparar o prato.
• preparação_time (int): Tempo de preparação em minutos.
Execução da API
Para executar uma API localmente, siga os passos abaixo:
1. 
Clonar ou repositório :
bater
Copiar código
git clone git@github.com:nomeusuario/gourmet-express-api.git
cd gourmet-express-api
2. 
Crie um ambiente virtual (opcional, mas recomendado) :
bater
Copiar código
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
3. 
Instalar as dependências :
Crie um arquivo chamado requirements.txtcom o seguinte conteúdo:
texto simples
Copiar código
fastapi
uvicorn
E então instale as dependências:
bater
Copiar código
pip install -r requirements.txt
4. 
Executar uma API :
bater
Copiar código
uvicorn main:app --reload
O servidor estará disponível em http://localhost:8000.
Conclusão
A API Gourmet Express é uma maneira simples e eficaz de acessar receitas de pratos variados. Sinta-se à vontade para explorar e integrar esta API em seus projetos. Para mais informações ou para contribuir, consulte o repositório do GitHub.
