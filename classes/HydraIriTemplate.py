from EPOS import Node

class HydraIriTemplate(Node):

  def __init__(self, *args): 
    self.type = self.hydra.IriTemplate
    Node.__init__(self, args) 
