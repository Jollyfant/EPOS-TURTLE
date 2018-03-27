from EPOS import Node

class Standard(Node):

  def __init__(self, *args): 
    self.type = self.dct.Standard
    Node.__init__(self, args)
