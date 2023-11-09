from api import app
from flask import jsonify
from flask_jwt_extended import JWTManager
from api.models.user_model import User

jwt = JWTManager(app)

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.get(identity)

@jwt.expired_token_loader
def expired_token_loader(algorithm, jwt_data):
    return jsonify({
        "message": "El token ha caducado."
    }), 401

@jwt.unauthorized_loader
def unauthorized_loader(error_message):
    return jsonify({
        "message": "Token ausente."
    }), 401