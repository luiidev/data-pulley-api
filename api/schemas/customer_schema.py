from marshmallow import Schema, fields, validate, EXCLUDE, post_load, pre_dump
from api.models.customer_model import Customer
# from api.schemas.user_schema import UserSchema
from api.schemas.payment_method_schema import PaymentMethodSchema


class CustomerSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model: Customer
        fields = [
            "id",
            "user_id",
            "country",
            "name",
            "employe_number",
            "sector",
            "areas",
            "platforms",
            "payment_method_id",
            "invoice_required",
            "ruc",
            "address",
            "profile_image_url",
            "banner_image_url",
            "state",
            "created_at",
            "updated_at",
            "user",
            "payment_method",
        ]
        exclude = ["id", "user_id", "state", "created_at", "updated_at"]

    # user = fields.Nested("UserSchema", exclude=["analyst", "customer", "password"])
    payment_method = fields.Nested("PaymentMethodSchema")

    country = fields.Integer(required=True)
    name = fields.String(required=True)
    employe_number = fields.Integer(required=True)
    sector = fields.String(required=True)
    areas = fields.List(fields.String(validate=validate.Length(min=1, max=25)))
    platforms = fields.List(fields.String(validate=validate.Length(min=1, max=25)))
    invoice_required = fields.Boolean(required=True)
    ruc = fields.String(required=True)
    address = fields.String(required=True)

    def clear_str(self, item):
        return item.strip().replace(",", "_").upper()

    @post_load(pass_many=True)
    def post_load(self, data, many, **kwargs):
        if "areas" in data:
            areas = map(self.clear_str, data["areas"])
            data["areas"] = ",".join(areas)

        if "platforms" in data:
            platforms = map(self.clear_str, data["platforms"])
            data["platforms"] = ",".join(platforms)

        return data

    @pre_dump()
    def pre_dump(self, data: Customer, many, **kwargs):
        if data.areas: 
            data.areas = data.areas.split(",")
        if data.platforms:
            data.platforms = data.platforms.split(",")

        return data
