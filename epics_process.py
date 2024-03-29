from node import *
from score import *
import pandas as pd
from draw_graph import *

def create_graph(df):
    anodes = AllNodes()
    for _, row in df.iterrows():
      parent_id = row['requirement']
      child_id = row['dependency epic']
      epic_type = row['dependency']
      score = row['score']
      parent_node = None
      print(f"parent id {parent_id} child id{child_id} epic type{epic_type} score{score}")
      # check if parent exists - if no create
      if anodes.does_exist(id=parent_id) == False :
        print(f" creating new parent node {parent_id}")
        parent_node = anodes.create_node(parent_id,"FUNC")
      else:
        parent_node = anodes.get_node(parent_id)
      # create child Node
      child_node = anodes.create_node(child_id,epic_type=epic_type,dep_score=score)
      anodes.add_dependency(parent=parent_node,child=child_node)
    
    return anodes

def process_calc_draw(xls_name , options):
    # Step 1 - read xls into dataframe
    # Step 2 - calculate score for every dependency 
    # Step 3 - Create a graph , pick up parent nodes list 
    # Step 4 - draw the graph
    # implement step 1 
    df = pd.read_excel(xls_name,'dependency')
    # calculate score , step 2
    row_iterate_score(df)
    # create the graph 
    anodes = create_graph(df)
    # get top parent nodes 
    parent_nodes = anodes.sort_parents()
    # draw the graph 
    g = draw_allsubgraphs(parent_nodes)
    g.render('result',format='svg',view=False)
      
    return None




