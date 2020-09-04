
from marshmallow import Schema, fields
import datetime as dt

class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 
        self.publish_date = dt.datetime.now()

class AuthorSchema(Schema):
    name = fields.String()
    email = fields.Email()


class BookSchema(Schema):
    title = fields.String()
    publish_date = fields.DateTime()
    author = fields.Nested(AuthorSchema)


"""
    nested self
"""

class TreeNode():
    def add_child(self, n):
        self.children.append(n)

    def __init__(self, v):
        self.val = v
        self.children = []

class TreeNodeSchema(Schema):
    val = fields.String()
    children = fields.List(fields.Nested(lambda: TreeNodeSchema()))



