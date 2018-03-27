from EPOS import Node

class Frequency(Node):

  def __init__(self, *args): 
    self.type = self.dct.Frequency
    Node.__init__(self, args) 
