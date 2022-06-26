import hashlib, base64
import hmac
import json
from flask import request
from flask_restx import abort
from project.config import BaseConfig
import jwt

from project.exceptions import InvalidTokens
from project.schemas.user import UserSchema
from datetime import datetime, timedelta


def read_json(filename, encoding="utf-8"):
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def get_hash_by_password(password: str):
    hashed = hashlib.pbkdf2_hmac(hash_name=BaseConfig.HASH_NAME,
                                 salt=BaseConfig.HASH_SALT.encode("utf-8"),
                                 iterations=BaseConfig.HASH_ITERATIONS,
                                 password=password.encode("utf-8"))
    return base64.b64encode(hashed).decode("utf-8")


def generate_tokens(user: UserSchema):
    payload_access = {
        "email": user["email"],
        "id": user["id"],
        "exp": datetime.utcnow() + timedelta(minutes=BaseConfig.TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(
        payload=payload_access,
        key=BaseConfig.SECRET_KEY,
        algorithm=BaseConfig.JWT_ALGO
    )

    payload_refresh = {
        "email": user["email"],
        "id": user["id"],
        "exp": datetime.utcnow() + timedelta(days=BaseConfig.TOKEN_EXPIRE_DAYS)
    }
    refresh_token = jwt.encode(
        payload=payload_refresh,
        key=BaseConfig.SECRET_KEY,
        algorithm=BaseConfig.JWT_ALGO
    )

    tokens = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    return tokens


def compare_passwords(password_hash: str, password_other: str):
    return hmac.compare_digest(password_hash, password_other)


def decode_token(token: str):
    decoded_token = {}
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=BaseConfig.SECRET_KEY,
            algorithms=[BaseConfig.JWT_ALGO]
            )
    except InvalidTokens:
        abort(401)
    return decoded_token


def get_id_from_token(token):
    token = decode_token(token)
    uid = token.get("id")
    return uid


def generate_new_tokens(refresh_token):
    decoded_token = decode_token(refresh_token)
    data = {
        "id": decoded_token["id"],
        "email": decoded_token["email"]
    }
    tokens = generate_tokens(data)
    return tokens


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401, message="field 'Authorization' not in headers")
        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(
                jwt=token,
                key=BaseConfig.SECRET_KEY,
                algorithms=[BaseConfig.JWT_ALGO]
            )
        except InvalidTokens:
            abort(401)
        return func(*args, **kwargs)
    return wrapper

