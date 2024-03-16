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

def draw_node(node : Node,dot):
    #dot.format = 'svg'
    dot.node(name=str(id(node)), label = "{  %s | dep_score %.4f }" % (node.id ,node.get_dependency_score()), shape='record')
    if node.children_length() > 0 :
      for child in node._children:
        dot.edge(str(id(node)), str(id(child)))
            

def draw_full_tree(root,dot):
    print(f" dot format is {dot.format}")
    if root:
      for node in root._children:
        draw_full_tree(node,dot)
      draw_node(root,dot)

def draw_subgraph_node(node,c):
    c.node(name=str(id(node)), label = "{  %s | dep_score %.4f }" % (node.id ,node.get_dependency_score()), shape='record')
    if node.children_length() > 0 :
      for child in node._children:
        c.edge(str(id(node)), str(id(child)))
   
    return None

def postorder_draw(root : Node,c ):
    """
      Args:
      root (Node): 
      Do a postorder traversal of tree of nodes in order to draw 
      1) visit children , draw them in a subgraph 
      2) visit parent , draw it in a subgraph
    """
    if root:
      for node in root._children:
        postorder_draw(node,c)
      draw_subgraph_node(root,c)

def draw_subgraph(g,root):
    with g.subgraph(name='cluster_0') as c:
      c.attr(style='filled', color='lightgrey')
      c.node_attr.update(style='filled', color='white')
      postorder_draw(root,c)
      
      