from marshmallow import Schema, fields, validate


class CreateSignupInputSchema(Schema):
    # the 'required' argument ensures the field exists
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    nic = fields.Str(required=True)
    contact = fields.Str(required=True, validate=validate.Length(min=10, max=10))
    password = fields.Str(required=True, validate=validate.Length(min=6))
