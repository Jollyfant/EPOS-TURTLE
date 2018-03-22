from EPOS import Node

class HydraIriTemplate(Node):

  ALLOWED = [
    "hydra:template",
    "hydra:mapping"
  ]

  def __init__(self, *args): 
    Node.__init__(self, args) 
    self.type = self.hydra.IriTemplate
