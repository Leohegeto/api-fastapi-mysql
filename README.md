API FastAPI MySQL
Este é um projeto de API RESTful desenvolvida com FastAPI e integrada ao MySQL. Ele oferece operações básicas de CRUD (Criar, Ler, Atualizar, Deletar) para gerenciamento de dados.

Funcionalidades
CRUD: Permite criar, ler, atualizar e excluir registros no banco de dados MySQL.

FastAPI: Framework utilizado para construção de APIs rápidas e de alta performance.

MySQL: Banco de dados relacional para armazenar os dados.

Tecnologias Utilizadas
FastAPI: Framework para criação de APIs de alto desempenho.

MySQL: Banco de dados relacional utilizado para persistência de dados.

Pydantic: Para validação de dados e definição de schemas.

SQLAlchemy: ORM para facilitar a interação com o banco de dados MySQL.

Como Rodar o Projeto
1. Clone o repositório
Clone este repositório para sua máquina local:

git clone https://github.com/SEU-USUARIO/api-fastapi-mysql.git
2. Instale as dependências
Navegue até a pasta do projeto e instale as dependências com:

cd api-fastapi-mysql
pip install -r requirements.txt
3. Configure o banco de dados
Antes de rodar a aplicação, configure o banco de dados MySQL:

Crie um banco de dados no MySQL:

mysql -u root -p
CREATE DATABASE nome_do_banco;
Altere as credenciais no arquivo de configuração para que o projeto se conecte ao banco de dados.

4. Rode a aplicação
Execute o servidor FastAPI com o comando:

uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000.

5. Acesse a documentação da API
O FastAPI gera uma documentação interativa automaticamente. Após rodar a aplicação, acesse:

http://127.0.0.1:8000/docs

Como Contribuir
Faça um fork deste repositório.

Crie uma nova branch para suas modificações (git checkout -b minha-nova-feature).

Realize suas alterações e commit com mensagens claras (git commit -am 'Adiciona nova funcionalidade X').

Envie suas modificações para o repositório remoto (git push origin minha-nova-feature).

Abra um pull request explicando suas alterações.

Licença
Este projeto está licenciado sob a MIT License.