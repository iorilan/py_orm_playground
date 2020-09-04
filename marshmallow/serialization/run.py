import os,sys
from schema import *
from datetime import datetime
from pprint import pprint

def serialize():
    dtfmt = '%Y-%m-%dT%H:%M:%S'
    student = Student(
        name="jeo",
        email="jeo@stu.com",
        id=1,
        age=20,
        graduated=False,
        dob=datetime.strptime('2001-01-01T11:00:00',dtfmt))
    

    schema = SchemaStudent()
    res1 = schema.dump(student)
    print('common===>')
    pprint(res1)
    
    schema2_class = Schema.from_dict(
        {
            "name":fields.Str(), 
            "email":fields.Email(),
            "some_other_field":fields.Str()
        })
    schema2 = schema2_class()
    res2 = schema2.dump(student)
    print('dict===>')
    pprint(res2)

    #will throw error
    #SchemaStudent(only=("name","id","invalid"))
    schema3 = SchemaStudent(only=("name","id","dob"))
    res3 = schema3.dump(student)
    print('only===>')
    pprint(res3)

    mike = Student("mike","mike@stu.com",2,34,datetime.strptime("1980-01-03T15:30:31",dtfmt),True)
    stuArr = [student,mike]
    schema4 = SchemaStudent(many=True)
    res4 = schema4.dump(stuArr)
    print('Array ==>')
    pprint(res4)
    

def deserialize():
    json_str = '{"name":"mike","id":2,"age":21,"dob":"2002-02-03T14:45:21","email":"mike@stu.com"}'
    #extra field will throw error
    import json
    json_dict = json.loads(json_str)
    schema = SchemaStudent()
    obj = schema.load(json_dict)
    pprint(obj)

if __name__ == "__main__":
    serialize()
    deserialize()
