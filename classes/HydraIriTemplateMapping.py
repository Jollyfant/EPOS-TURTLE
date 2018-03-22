from EPOS import Node

class HydraIriTemplateMapping(Node):

  ALLOWED = [
    "hydra:variable",
    "hydra:required",
    "schema:minValue",
    "schema:maxValue",
    "schema:defaultValue"
  ]

  def __init__(self, *args): 
    Node.__init__(self, args) 
    self.type = self.hydra.IriTemplateMapping
