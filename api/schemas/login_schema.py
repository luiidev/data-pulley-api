from marshmallow import Schema, fields, validate, EXCLUDE
from api.error_messages import field_error_messages

fields.Field.default_error_messages = field_error_messages

class LoginSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    email = fields.String(
        required=True,
        validate=validate.Email(error="La dirección de email no es válida."),
    )
    password = fields.String(required=True)
