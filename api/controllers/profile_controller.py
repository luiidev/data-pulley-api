from api import api
from flask import jsonify, request
from flask_jwt_extended import jwt_required, current_user
from marshmallow import ValidationError
from api.models.user_model import User
from api.models.analyst_model import Analyst
from api.models.customer_model import Customer
from api.schemas.analyst_schema import AnalystSchema
from api.schemas.customer_schema import CustomerSchema
from api.schemas.user_schema import UserSchema
from api.database import db_session

@api.get("/profile/analyst")
@jwt_required()
def get_analyst_profile():
    user = User\
        .with_join(User.analyst)\
        .where(User.id==current_user.id)\
        .first()
    
    return jsonify({
        "message": "",
        "data": UserSchema(exclude=["customer", "password"]).dump(user)
    })

@api.put("/profile/analyst")
@jwt_required()
def update_analyst_profile():
    try:
        analystSchema = AnalystSchema().load(request.json)
        userSchema = UserSchema(exclude=["email"]).load(request.json)
    except ValidationError as e:
        return jsonify({"message": "Error en validación de campos.", "errors": e.messages}), 422

    if analystSchema:
        Analyst.query.where(Analyst.user_id==current_user.id).update(analystSchema)

    if userSchema:
        User.query.where(User.id==current_user.id).update(userSchema)
        
    db_session.commit()
        
    user = User\
        .with_join(User.analyst)\
        .where(User.id==current_user.id)\
        .first()

    return jsonify({
        "message": "",
        "data": UserSchema(exclude=["customer", "password"]).dump(user)
    })

@api.get("/profile/customer")
@jwt_required()
def get_customer_profile():
    user = User\
        .with_join(User.customer)\
        .where(User.id==current_user.id)\
        .first()
    
    return jsonify({
        "message": "",
        "data": UserSchema(exclude=["analyst", "password"]).dump(user)
    })

@api.put("/profile/customer")
@jwt_required()
def update_customer_profile():
    try:
        customerSchema = CustomerSchema().load(request.json)
        userSchema = UserSchema(exclude=["email"]).load(request.json)
    except ValidationError as e:
        return jsonify({"message": "Error en validación de campos.", "errors": e.messages}), 422

    if customerSchema:
        Customer.query.where(Customer.user_id==current_user.id).update(customerSchema)

    if userSchema:
        User.query.where(User.id==current_user.id).update(userSchema)
        
    db_session.commit()

    user = User\
        .with_join(User.customer)\
        .where(User.id==current_user.id)\
        .first()

    return jsonify({
        "message": "",
        "data": UserSchema(exclude=["analyst", "password"]).dump(user)
    })