from node import *
from draw_graph import * 
from graphviz import Digraph


def test_subgraph2():
    anodes = AllNodes()
    n = anodes.create_node("P2G-100","FUNC")
    d = anodes.create_node("GDB-100","DEVOPS")
    d1 = anodes.create_node("PCM-100","INFRA")
    anodes.add_dependency(n,d)
    anodes.add_dependency(n,d1)
    # 2nd parent node
    n1 = anodes.create_node("P2G-101","FUNC")
    d11 = anodes.create_node("GDB-101","DEVOPS")
    d12 = anodes.create_node("PCM-102","INFRA") 
    anodes.add_dependency(n1,d11)
    anodes.add_dependency(n1,d12)
    _,parents = anodes.get_top_parents()
    g= draw_allsubgraphs(parents)
    return g

def test_graph():
  # Create a new directed graph
  dot = Digraph(comment='The Round Table')

  # Adding nodes and edges
  dot.node('A', 'King Arthur')
  dot.node('B', 'Sir Bedevere the Wise')
  dot.node('L', 'Sir Lancelot the Brave')

  dot.edges(['AB', 'AL'])
  dot.edge('B', 'L', constraint='false')


  # Render the graph to a file in SVG format
  dot.render('round_table', format='svg', view=False)
   
    