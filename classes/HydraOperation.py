from EPOS import Node

class HydraOperation(Node):

  def __init__(self, *args): 
    self.type = self.hydra.Operation
    Node.__init__(self, args)
