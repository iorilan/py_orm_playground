from marshmallow import Schema, fields, validates_schema, validate, ValidationError

def valid_pwd(pwd):
    if len(pwd)<8:
        return False
    has_digit = False
    has_upper = False
    has_lower = False
    for c in pwd:
        s = str(c)
        if s.isdigit():
            has_digit = True
        if s.isupper():
            has_upper = True
        if s.islower():
            has_lower = True

    return has_lower and has_upper and has_digit

class UserSchema(Schema):
    id = fields.Int(required=True)
    firstname = fields.Str(data_key="name", required=True)
    lastname = fields.Str(required=True)
    password = fields.Str(validate=valid_pwd)
    level = fields.Integer(required=True, validate=validate.OneOf([1,2,3]))
    age = fields.Integer(validate=validate.Range(min=15,max=20))
    # more validators https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html#marshmallow.validate.OneOf

    @validates_schema
    def class_level(self, data, **kwargs):
        if len(data["firstname"]) + len(data["lastname"]) > 20:
            raise ValidationError({"class_level_error":"name too long !!"})
    
    """
    custom error handling
    def handle_error(self, exc, data, **kwargs):
        logging.error(exc.messages)
        raise AppError("An error occurred ")
        ...
    """