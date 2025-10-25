import os
#import hashlib
from datetime import timedelta

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from granian import Granian
from granian.constants import Interfaces


app = Flask(__name__)

# python -c "import secrets; print(secrets.token_hex())"
app.config["JWT_SECRET_KEY"] = '81e475733a14453c846ec83d2221fe8f0bb8770a2b2c1c1f45d44a291a750726'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

bcrypt = Bcrypt(app)

auth = HTTPBasicAuth()

users_db = {
    "dead-duck": {
        "password_hash": bcrypt.generate_password_hash("senha_segura").decode('utf-8')
    },
    "bob-cuspe": {
        "password_hash": bcrypt.generate_password_hash("outra_senha").decode('utf-8')
    }
}

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, Dead Duck!"


@auth.verify_password
def verify_password(username, password):
    """
    Função de callback do Flask-HTTPAuth para verificar as credenciais.
    """
    if username in users_db and bcrypt.check_password_hash(users_db[username]["password_hash"], password):
        return username
    return None


@app.route("/login", methods=["POST"])
@auth.login_required
def login():
    username = auth.current_user()
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/set", methods=["POST"])
@jwt_required()
def set_value():
    data = request.get_json()
    value = data.get("name")
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello {current_user}, You send value {value}"}), 201


def run():
    Granian(
        target='main:app',
        interface=Interfaces.WSGI,
        workers=1,
        backpressure=2
    ).serve()


# curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Basic USER:PASS|BASE64' http://127.0.0.1:8000/login
# curl -X POST -H 'Content-Type: application/json' -H 'Authorization: Bearer TOKEN' -d '{"name": "Dead Duck"}' http://127.0.0.1:8000/set