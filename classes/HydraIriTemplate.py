from EPOS import Node

class HydraIriTemplate(Node):

  ALLOWED = [
    "hydra:template",
    "hydra:mapping"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.hydra.IriTemplate
