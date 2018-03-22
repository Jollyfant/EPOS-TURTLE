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

  def __init__(self, *args): 
    Node.__init__(self, args)
    self.type = self.hydra.Operation
