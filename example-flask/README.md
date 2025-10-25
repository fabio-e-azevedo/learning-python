# Projeto API com Flask, Peewee e JWT

Uma API web segura desenvolvida em Python com Flask, utilizando Peewee para persistência de dados em um banco de dados SQLite e JWT (JSON Web Tokens) para autenticação. A API permite registrar novos usuários e proteger endpoints com autenticação.

Funcionalidades
- Registro de Usuário: Endpoint /register para criar novos usuários com senha segura (hash Bcrypt).
- Login: Endpoint /login para autenticar usuários via Basic Authentication.
- Autenticação JWT: Após o login, é gerado um token JWT de acesso que pode ser usado para autenticar outras requisições.
- Rotas Protegidas: O endpoint /set é protegido, exigindo um token JWT válido para ser acessado.
- Banco de Dados SQLite: Armazena os dados dos usuários em um arquivo local chamado users.db.

Como Executar

1. Inicializar o banco de dados
As tabelas do banco de dados são criadas automaticamente na inicialização da aplicação. Não há necessidade de um comando manual para este projeto.

2. Iniciar o servidor
Você pode iniciar a aplicação de duas formas:

Com comando "granian"
```shell
granian --interface wsgi --workers 1 --backpressure 2 --reload main:app
```

Com comando "uv run"
```shell
uv pip install -e .
uv run app
```

Como Usar a API

1. Registrar um novo usuário  
Endpoint: POST /register  
```shell
curl -X POST -H "Content-Type: application/json" -d '{"username": "dead-duck", "password": "secure-password"}' http://localhost:8000/register
```

  
2. Autenticar e obter um token JWT  
Endpoint: POST /login  
```shell
curl -X POST -u 'dead-duck:secure-password' http://localhost:8000/login

# OU a string "username:password" é codificada em Base64 e é enviada no cabeçalho Authorization, precedida pela palavra Basic

AUTH_BASIC_BASE64=$(echo -n 'dead-duck:secure-password' | base64)

curl -s -X POST -H "Authorization: Basic $AUTH_BASIC_BASE64" http://localhost:8000/login -o token.json
```

  
3. Acessar uma rota protegida (usando o token JWT)  
Endpoint: POST /set  
```shell
TOKEN_JWT=$(jq -r '.access_token' token.json)

curl -X POST -H 'Content-Type: application/json' -H "Authorization: Bearer $TOKEN_JWT" -d '{"name": "Dead Duck"}' http://localhost:8000/set
```
