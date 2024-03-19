
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
    def has_parent(self):
        return self._parent != None 
    def __repr__(self):
        return f"id({self.id}), dep score({self.__dep_score})"

class AllNodes:
    def __init__(self):
        self.nodes = {}
        # parents which does not have parents above them
        self.top_parents = set()
    def create_node(self,id, epic_type , dep_score=0,_children=()):
        n = Node(id, epic_type , dep_score,_children) 
        self.add_node(n)   
    def add_node(self,node):
        if not isinstance(node, Node):
          return NotImplemented
        self.nodes[node.id] = node
    def add_dependency(self,p,c):
        assert isinstance(p, Node)
        assert isinstance(c,Node) 
        if p.has_parent() == None:
          self.top_parents.add(p.id)
        if c.has_parent() != None:
          self.top_parents.remove(c.id)  
        p.add_dependency(c)
    def does_exist(self,id):
      if id in self.nodes:
        return True
      else: 
        return False
    def sort_parents(self):
        return None
    
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

def postorder_visit(root : Node):
    """
    _summary_
       Args:
      root (Node): 
      Do a postorder traversal of nodes 
      1) visit children , process them 
      2) visit parent , process parent.
    """
    if root:
      for node in root._children:
        postorder_visit(node)
      process_node(root)
          
              
            
      
       