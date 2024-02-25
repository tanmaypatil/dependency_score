import graphviz
from graphviz import Digraph
from node import * 
from IPython.display import display

dot = Digraph()

def draw_dot(root, format='svg', rankdir='LR'):
    """
    format: png | svg | ...
    rankdir: TB (top to bottom graph) | LR (left to right)
    """
    assert rankdir in ['LR', 'TB']
    nodes, edges = trace(root)
    dot = Digraph(format=format, graph_attr={'rankdir': rankdir}) #, node_attr={'rankdir': 'TB'})
    
    for n in nodes:
        dot.node(name=str(id(n)), label = "{ id %s | dep_score %.4f }" % (n.id, n.dep_score), shape='record')
        if n._op:
            dot.node(name=str(id(n)) + n._op, label=n._op)
            dot.edge(str(id(n)) + n._op, str(id(n)))
    
    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)
    
    return dot

def trace(root):
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._children:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges


def draw_tree(root, format='svg', rankdir='BT'):
    dot = Digraph(format=format, graph_attr={'rankdir': rankdir})
    c1 = Node("GDB-1000","DEVOPS",5)
    dot.node(name=str(id(c1)), label = "{ id %s | dep_score %.4f }" % (c1.id ,c1.get_dependency_score()), shape='record')
    c2 = Node("PCM-1001","INFRA",5)
    dot.node(name=str(id(c1)), label = "{ id %s | dep_score %.4f }" % (c2.id ,c2.get_dependency_score()), shape='record')
    return dot