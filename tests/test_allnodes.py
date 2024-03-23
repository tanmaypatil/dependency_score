from node import *
def test_create():
    assert 1 == 1

def test_create_node():
    anodes = AllNodes()
    n = anodes.create_node("P2G-100","FUNC")
    assert anodes.does_exist(n) == True
    assert anodes.is_top_parent(n) == True

def test_simple_dep():
    anodes = AllNodes()
    n = anodes.create_node("P2G-100","FUNC")
    d = anodes.create_node("GDB-100","DEVOPS")
    anodes.add_dependency(n,d)
    assert anodes.does_exist(n) == True
    assert anodes.does_exist(d) == True
    assert anodes.is_top_parent(n) == True
    assert anodes.is_top_parent(d) == False

def test_simple_dep1():
    anodes = AllNodes()
    n = anodes.create_node("P2G-100","FUNC")
    d = anodes.create_node("GDB-100","DEVOPS")
    d1 = anodes.create_node("PCM-100","INFRA")
    anodes.add_dependency(n,d)
    anodes.add_dependency(n,d1)
    assert anodes.does_exist(n) == True
    assert anodes.does_exist(d) == True
    assert anodes.is_top_parent(n) == True
    assert anodes.is_top_parent(d) == False
    assert anodes.is_top_parent(d1) == False
    assert anodes.count_parents() == 1

def test_simple_dep2():
    anodes = AllNodes()
    n = anodes.create_node("P2G-100","FUNC")
    d = anodes.create_node("GDB-100","DEVOPS")
    d1 = anodes.create_node("PCM-100","INFRA")
    anodes.add_dependency(n,d)
    anodes.add_dependency(n,d1)
    assert anodes.does_exist(n) == True
    assert anodes.does_exist(d) == True
    assert anodes.is_top_parent(n) == True
    assert anodes.is_top_parent(d) == False
    assert anodes.is_top_parent(d1) == False
    assert anodes.count_parents() == 1 
    # 2nd parent node
    n1 = anodes.create_node("P2G-101","FUNC")
    d11 = anodes.create_node("GDB-101","DEVOPS")
    d12 = anodes.create_node("PCM-102","INFRA") 
    anodes.add_dependency(n1,d11)
    anodes.add_dependency(n1,d12)
    assert anodes.count_parents() == 2
    assert anodes.count_all() == 6
    parents,_ = anodes.get_top_parents()
    expected = list()
    expected = expected + list( ["P2G-100","P2G-101"])
    assert expected == parents

def test_simple_dep2():
    anodes = AllNodes()
    n = anodes.create_node("P2G-100","FUNC")
    d = anodes.create_node("GDB-100","DEVOPS")
    d1 = anodes.create_node("PCM-100","INFRA")
    anodes.add_dependency(n,d)
    anodes.add_dependency(n,d1)
    assert anodes.does_exist(n) == True
    assert anodes.does_exist(d) == True
    assert anodes.is_top_parent(n) == True
    assert anodes.is_top_parent(d) == False
    assert anodes.is_top_parent(d1) == False
    assert anodes.count_parents() == 1 
    n1 = anodes.create_node("P2G-200","FUNC")
    anodes.add_dependency(parent=n1,child=n)
    assert anodes.count_parents() == 1
    parents,_ = anodes.get_top_parents()
    expected = list()
    expected.append("P2G-200")
    assert parents == expected
       
    