from pprint import pprint
import schema 

def test1():
    a = schema.Author(name="Leo", email="leo@kite.com")
    b = schema.Book(title="very good", author=a)
    result = schema.BookSchema().dump(b)
    pprint(result)

def test2():
    n = schema.TreeNode('1')
    n.add_child(schema.TreeNode("1-1"))
    n.children[0].add_child( schema.TreeNode('1-1-1'))
    n.add_child( schema.TreeNode("1-2"))
    n.children[1].add_child( schema.TreeNode('1-2-1'))
    result = schema.TreeNodeSchema().dump(n)
    pprint(result, indent=2)
    
if __name__ == "__main__":
    test1()
    test2()