from EPOS import Node

class HydraOperation(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "hydra:method",
    "hydra:returns",
    "hydra:IriTemplate"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.hydra.Operation
