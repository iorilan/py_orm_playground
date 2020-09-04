from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    password = fields.Str()
    created = fields.DateTime()

    class Meta:
        load_only = ['password']
        datetimeformat = '%Y-%m-%dT%H:%M:%SZ'

""" meta options: 
    fields: list of fields to include in the serialized result, can be used to remove the need of explicitly defining each field,
    additional: list of fields to include in addition to the explicitly defined fields,
    exlude: list of fields to exclude from the schema, will throw unknown field validation error at deserialization and will omit at serialization,
    dateformat and datetimeformat: defines the format of the date and the datetime ,
    ordered: preserve the order of the schema definition,
    load_only: specify fields to exclude during serialization, similar to schema args,
    dump_only: specify fields to exclude during deserialization, similar to schema args,
    unknown: the behavior to take on unknown fields (EXCLUDE, INCLUDE, RAISE), similar to schema args,
"""