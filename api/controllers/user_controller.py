from api import api
from flask import jsonify
from flask_jwt_extended import jwt_required
from api.models.user_model import User
from api.schemas.user_schema import UserSchema

from sqlalchemy.orm import joinedload

@api.route("/users")
@jwt_required()
def get():
    users = User.with_join(User.analyst, User.customer).all()

    usersSchema = UserSchema(many=True, exclude=["analyst", "password"]).dump(users)

    return jsonify({"message": "OK", "data": usersSchema})
