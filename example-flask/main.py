import os
import secrets
from datetime import timedelta
from werkzeug.exceptions import BadRequest

import peewee
from flask import Flask, request, jsonify, g
from flask_bcrypt import Bcrypt
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)
from granian import Granian
from granian.constants import Interfaces
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", secrets.token_hex(32))
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
auth = HTTPBasicAuth()

DATABASE = os.getenv("DATABASE_PATH", "users.db")
database = peewee.SqliteDatabase(DATABASE)


class User(peewee.Model):
    username = peewee.CharField(unique=True, index=True)
    password_hash = peewee.CharField()

    class Meta:
        database = database


def initialize_database():
    database.connect()
    database.create_tables([User], safe=True)
    database.close()


initialize_database()


def get_db():
    if not hasattr(g, "db"):
        g.db = database
        g.db.connect()
    return g.db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, "db", None)
    if db is not None:
        db.close()


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, Dead Duck!"


@auth.verify_password
def verify_password(username, password):
    """
    Flask-HTTPAuth callback function to verify credentials.
    """
    user = User.get_or_none(User.username == username)
    if user and bcrypt.check_password_hash(user.password_hash, password):
        return username
    return None


@app.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
    except BadRequest:
        return jsonify({"message": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if User.select().where(User.username == username).exists():
        return jsonify({"message": "Username already exists"}), 409

    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    User.create(username=username, password_hash=password_hash)
    return jsonify({"message": "User registered successfully"}), 201


@app.route("/login", methods=["POST"])
@auth.login_required
def login():
    username = auth.current_user()
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/set", methods=["POST"])
@jwt_required()
def set_value():
    try:
        data = request.get_json()
    except BadRequest:
        return jsonify({"message": "Invalid JSON"}), 400

    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello {current_user}, you sent the data: {data}"}), 201


def run():
    Granian(
        target="main:app", interface=Interfaces.WSGI, workers=1, backpressure=2
    ).serve()
