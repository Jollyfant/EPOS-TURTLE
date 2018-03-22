from EPOS import Node

class HydraClass(Node):

  ALLOWED = [
    "hydra:supportedProperty"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.hydra.Class
