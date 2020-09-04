from marshmallow import Schema, fields, INCLUDE, ValidationError
class Student:
    def __init__(self, name, email, id, age, dob, graduated):
        self.name = name
        self.email = email
        self.id = id
        self.age = age
        self.dob = dob
        self.graduated = graduated
    

class SchemaStudent(Schema):
    name = fields.Str()
    email = fields.Email()
    id = fields.Int()
    age = fields.Int()
    dob = fields.DateTime()
    graduated = fields.Boolean()
