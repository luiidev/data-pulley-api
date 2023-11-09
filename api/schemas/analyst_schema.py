from marshmallow import Schema, fields, validate, EXCLUDE, post_load, pre_dump
from api.models.analyst_model import Analyst
# from api.schemas.user_schema import UserSchema
from api.schemas.payment_method_schema import PaymentMethodSchema


class AnalystSchema(Schema):
    class Meta:
        unknown = EXCLUDE
        model: Analyst
        fields = [
            "id",
            "user_id",
            "country",
            "years_experience",
            "cost_hour",
            "tools",
            "about",
            "payment_method_id",
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
    years_experience = fields.Integer(required=True)
    cost_hour = fields.Float(required=True)
    tools = fields.List(fields.String(validate=validate.Length(min=1, max=25)))
    about = fields.String(required=True, validate=validate.Length(min=50))

    def clear_str(self, item):
        return item.strip().replace(",", "_").upper()

    @post_load(pass_many=True)
    def clear_tools(self, data, many, **kwargs):
        tools = map(self.clear_str, data["tools"])
        data["tools"] = ",".join(tools)

        return data

    @pre_dump()
    def tools_to_str(self, data: Analyst, many, **kwargs):
        data.tools = data.tools.split(",")

        return data
