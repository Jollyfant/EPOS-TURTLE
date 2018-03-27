from EPOS import Node

class RDFSLiteral(Node):

  def __init__(self, *args): 
    self.type = self.dct.RDFSLiteral
    Node.__init__(self, args) 
