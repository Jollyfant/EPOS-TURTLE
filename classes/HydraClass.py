from EPOS import Node

class HydraClass(Node):

  ALLOWED = [
    "hydra:supportedProperty"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.hydra.Class
