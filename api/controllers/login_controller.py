from api import api
from flask import request, jsonify
from flask_jwt_extended import create_access_token
import datetime
from api.models.user_model import User
from api.schemas.user_schema import UserSchema
from api.schemas.login_schema import LoginSchema


@api.post("/login")
def login():
    errors = LoginSchema().validate(request.json)

    if errors:
        return jsonify({"message": "Error en validación de campos.", "errors": errors})

    email = request.json.get("email")
    password = request.json.get("password")

    user = User.query.where(User.email == email).first()

    if not user or not user.verify_password(password):
        return jsonify({"message": "Correo o contraseña incorrecta."}), 401

    token = create_access_token(identity=user, expires_delta=datetime.timedelta(days=7))

    return jsonify(
        {
            "message": "Inicio de sesión exitoso",
            "data": {"user": UserSchema(exclude=["password"]).dump(user), "token": token},
        }
    )
