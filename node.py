
class Node:
    def __init__(self, id, epic_type , dep_score=1,_children=(), _op=''):
      self.id = id
      self.epic_type = epic_type
      self.__dep_score = dep_score
      self._children = set(_children)
      self._parent = None
      self._op = _op # the op that produced this node, for graphviz / debugging / etc
    def add_dependency(self, other):
      other = other if isinstance(other, Node) else Node(other)
      self.__dep_score = self.__dep_score + other.__dep_score
      print(f"After adding child dependency {other.__dep_score} , parent dependency score{self.__dep_score}")
      #add the dependency to child list
      self._children.add(other)
      # set the parent on the other node
      other._parent = self
    def calc_dependency_score(self):
        self.__dep_score = 1
        return self.__dep_score 
    def children_lengh(self):
      return len(self._children)
       