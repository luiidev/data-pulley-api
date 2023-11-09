from marshmallow import Schema
from api.models.payment_method_model import PaymentMethod


class PaymentMethodSchema(Schema):
    class Meta:
        model: PaymentMethod
        fields = [
            "id",
            "name",
            "state",
            "created_at",
            "updated_at",
        ]
        exclude = ["state", "created_at", "updated_at"]
