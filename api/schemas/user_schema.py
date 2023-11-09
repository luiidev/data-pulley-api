from marshmallow import Schema, fields, validate, EXCLUDE, post_load
from werkzeug.security import generate_password_hash
from api.models.user_model import User
from api.schemas.analyst_schema import AnalystSchema
from api.schemas.customer_schema import CustomerSchema

class UserSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "role",
            "state",
            "created_at",
            "updated_at",
            "analyst",
            "customer"
        ]
        exclude = ["role", "state", "created_at", "updated_at"]

    analyst = fields.Nested("AnalystSchema")
    customer = fields.Nested("CustomerSchema")

    email = fields.String(
        required=True,
        validate=validate.Email(error="La dirección de email no es válida."),
    )
    password = fields.String(validate=validate.Length(min=8, max=24))
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    
    @post_load(pass_many=True)
    def post_load(self, data, many, **kwargs):
        if "password" in data:
            data["password"] = generate_password_hash(data["password"])
        
        if "first_name" in data:
            data["first_name"] = data["first_name"].title()
        
        if "last_name" in data:
            data["last_name"] = data["last_name"].title()

        return data