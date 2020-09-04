
import datetime
from schema import UserSchema

if __name__ == "__main__":
    
    data = dict(name='test', age=11, password='123', created=datetime.datetime.now())
    schema = UserSchema()
    json_obj = schema.dump(data)
    print(json_obj)

    obj2=schema.load({'password': '123', **json_obj})
    print(obj2)
