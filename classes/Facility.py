from EPOS import Node

class Facility(Node):

  def __init__(self, *args): 
    self.type = self.epos.Facility
    Node.__init__(self, args) 
