from EPOS import Node

class Publication(Node):

  def __init__(self, *args): 
    self.type = self.epos.Publication
    Node.__init__(self, args)
