from EPOS import Node

class Identifier(Node):

  def __init__(self, *args): 
    self.type = self.dct.Identifier
    Node.__init__(self, args) 
