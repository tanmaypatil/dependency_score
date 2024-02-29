
from Stack import Stack
class Node:
    def __init__(self, id, epic_type , dep_score=0,_children=()):
      self.id = id
      self.epic_type = epic_type
      self.__dep_score = dep_score
      self._children = set(_children)
      self._parent = None
    def add_dependency(self, other):
      other = other if isinstance(other, Node) else Node(other)
      self.__dep_score = self.__dep_score + other.__dep_score
      print(f"After adding child dependency {other.__dep_score} , parent dependency score{self.__dep_score}")
      #add the dependency to child list
      self._children.add(other)
      # set the parent on the other node
      other._parent = self
    def calc_dependency_score(self):
        return self.__dep_score 
    def children_length(self):
      return len(self._children)
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.id == other.id and self.epic_type == other.epic_type
    def __hash__(self):
        return hash((self.id, self.epic_type))  
    def get_dependency_score(self):
        return self.__dep_score
    def set_dependency_score(self,dep_score):
        self.__dep_score = dep_score
    
def process_node(current_node):
    print("process_node ")
    print(f"current node id : {current_node.id} epic type : {current_node.epic_type}")
    # update self dependency score using summation of children score
    dep_score = 0 
    if len(current_node._children) > 0 :
      for node in current_node._children:
        dep_score += node.get_dependency_score()
      current_node.set_dependency_score(dep_score)
    print(f"childrens : {len(current_node._children)} , dependency score {current_node.get_dependency_score()}")
     

def dfs_visit(root):
    visited = set() 
    stack = Stack()
    stack.push(root)
    while not stack.is_empty():
      current_node = stack.pop()
      if current_node not in visited:
        process_node(current_node)
        visited.add(current_node)
        for node in current_node._children:
          if node not in visited:
            stack.push(node)

def postorder_visit(root):
    if root:
      for node in root._children:
        postorder_visit(node)
      process_node(root)
          
              
            
      
       