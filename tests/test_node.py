from node import *

def test_node_init():
    n = Node("P2G_123","FUNC")
    assert n.children_length() == 0

def test_dep_score():
    n = Node("P2G_123","FUNC")
    assert n.calc_dependency_score() == 0

    
def test_child_parent():
    p = Node("P2G-100","FUNC")
    c1 = Node("P2G-101","FUNC")
    c2 = Node("P2G-102","FUNC")
    p.add_dependency(c1)
    p.add_dependency(c2)
    assert p.children_length() == 2
    assert c1._parent.id == 'P2G-100'
    assert c2._parent.id == 'P2G-100'

def test_node_exists():
    s = set()
    e1 = Node("P2G-100","FUNC")
    s.add(e1)
    assert e1 in s

def test_node_notexists():
    s = set()
    e1 = Node("P2G-100","FUNC")
    s.add(e1)
    e2 = Node("P2G-101","FUNC")
    assert e2 not in s

def test_dfs():
    p = Node("P2G-100","FUNC")
    c1 = Node("P2G-101","FUNC")
    c2 = Node("P2G-102","FUNC")
    p.add_dependency(c1)
    p.add_dependency(c2)
    dfs_visit(p)
    
def test_postorder():
    p = Node("P2G-100","FUNC")
    c1 = Node("P2G-101","FUNC",1)
    c2 = Node("P2G-102","FUNC",2)
    p.add_dependency(c1)
    p.add_dependency(c2)
    postorder_visit(p)
    
def test_postorder_level2():
    p = Node("P2G-100","FUNC")
    c1 = Node("P2G-101","FUNC")
    c2 = Node("P2G-102","FUNC",2)
    p.add_dependency(c1)
    p.add_dependency(c2)
    c21 = Node("GDB-1234","DEVOPS",5)
    c22 = Node("PCM-1111","INFRA",5)
    c1.add_dependency(c21)
    c1.add_dependency(c22)
    postorder_visit(p)
    
def test_sort_nodes():
    n1 = Node("P2G-100","FUNC",5)
    n2 = Node("P2G-101","FUNC",15)
    n3 = Node("P2G-102","FUNC",25)
    n = set()
    n.add(n1)
    n.add(n2)
    n.add(n3)
    sorted_list = sorted(n,key=lambda  nd : nd.get_dependency_score() ,reverse=True)
    print(sorted_list)

    