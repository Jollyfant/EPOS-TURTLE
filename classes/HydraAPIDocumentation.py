from EPOS import Node

class HydraAPIDocumentation(Node):

  def __init__(self, *args):
    self.type = self.hydra.APIDocumentation
    Node.__init__(self, args) 
