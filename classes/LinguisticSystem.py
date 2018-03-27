from EPOS import Node

class LinguisticSystem(Node):

  def __init__(self, *args): 
    self.type = self.dct.LinguisticSystem
    Node.__init__(self, args) 
