from EPOS import Node

class RightsStatement(Node):

  def __init__(self, *args): 
    self.type = self.dct.RightsStatement
    Node.__init__(self, args) 
