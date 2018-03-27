from EPOS import Node

class ProvenanceStatement(Node):

  def __init__(self, *args): 
    self.type = self.dct.ProvenanceStatement
    Node.__init__(self, args) 
