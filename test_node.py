from node import Node
from requirement_load import load_req

def test_node_init():
    n = Node("P2G_123","FUNC")
    assert n.children_lengh() == 0

def test_dep_score():
    n = Node("P2G_123","FUNC")
    assert n.calc_dependency_score() == 1

def test_load_req():
    print("xyz")
    load_req()
    
def test_child_parent():
    p = Node("P2G-100","FUNC")
    c1 = Node("P2G-101","FUNC")
    c2 = Node("P2G-102","FUNC")
    p.add_dependency(c1)
    p.add_dependency(c2)
    assert p.children_lengh() == 2
    assert c1._parent.id == 'P2G-100'
    assert c2._parent.id == 'P2G-100'
    