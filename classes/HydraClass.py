from EPOS import Node

class HydraClass(Node):

  def __init__(self, *args): 
    self.type = self.hydra.Class
    Node.__init__(self, args) 
