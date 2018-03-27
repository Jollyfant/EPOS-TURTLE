from EPOS import Node

class Equipment(Node):

  def __init__(self, *args): 
    self.type = self.epos.Equipment
    Node.__init__(self, args) 
