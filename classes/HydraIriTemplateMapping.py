from EPOS import Node

class HydraIriTemplateMapping(Node):

  def __init__(self, *args): 
    self.type = self.hydra.IriTemplateMapping
    Node.__init__(self, args) 
