# Exemplo de um sistema com autenticação seguro.

# Start app command line granian
```shell
granian --interface wsgi --workers 1 --backpressure 2 --reload main:app
```

# Or start app with uv
```shell
uv pip install -e .
uv run app
```

```shell
curl -X POST -H "Content-Type: application/json" -d '{"username": "dead-duck", "password": "secure-password"}' http://localhost:8000/register
```

```shell
AUTH_BASIC_BASE64=$(echo -n 'dead-duck:secure-password' | base64)

curl -s -X POST -H 'Content-Type: application/json' -H "Authorization: Basic $AUTH_BASIC_BASE64" http://localhost:8000/login -o token.json

TOKEN_JWT=$(jq -r '.access_token' token.json)

curl -X POST -H 'Content-Type: application/json' -H "Authorization: Bearer $TOKEN_JWT" -d '{"name": "Dead Duck"}' http://localhost:8000/set
```