from marshmallow import Schema, fields, validate
class UserSchema(Schema):
    id = fields.Int()
    firstname = fields.Str(data_key="name")
    lastname = fields.Str(required=True)
    password = fields.Str()
    age = fields.Integer(required=True)