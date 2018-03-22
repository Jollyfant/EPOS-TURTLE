from EPOS import Node

class HydraIriTemplateMapping(Node):

  ALLOWED = [
    "hydra:variable",
    "hydra:required",
    "schema:minValue",
    "schema:maxValue",
    "schema:defaultValue"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, None, dictionary)
    self.type = self.hydra.IriTemplateMapping
