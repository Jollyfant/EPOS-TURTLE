from EPOS import Node

class Location(Node):

  def __init__(self, *args): 
    self.type = self.dct.Location
    Node.__init__(self, args) 
