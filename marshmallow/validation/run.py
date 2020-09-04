from schema import UserSchema
from marshmallow import Schema, ValidationError


def test(obj):
    try:
        print(UserSchema().load(obj))

    except ValidationError as err:
        print(err.messages)
    print('==================')
if __name__ == "__main__":
    """ 
        validation errors:
        {'level': ['Must be one of: 1, 2, 3.'], 'age': ['Must be greater than or equal to 15 and less than or equal to 20.'], 'password': ['Invalid value.'], 'id': ['Field may not be null.']}
    """
    test({
            'id':None,
            'name':'a',
            'lastname':'',
            'password':'aaa',
            'age':11,
            'level':None
        })
    test({
            'id':'a',
            'name':'',
            'lastname':'',
            'password':'',
            'age':21,
            'level':4
        })
    test({
            'id':1,
            'name':'longgggggggg',
            'lastname':'nammmmmmeee_trigger_schema_level_validation',
            'password':'aB1234567',
            'age':17, 
            'level':1
        })
    """
        valid
    """
    test({
            'id':1,
            'name':'a',
            'lastname':'b',
            'password':'aB1234567',
            'age':17, 
            'level':1
        })
    validate_result = UserSchema().validate({ 'id':'abc',
            'name':'',
            'lastname':'',
            'password':'aaa',
            'age':10, 
            'level':4})
    print(validate_result)