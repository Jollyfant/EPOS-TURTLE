from EPOS import Node

class HydraAPIDocumentation(Node):

  ALLOWED = [
    "hydra:description",
    "hydra:statusCode",
    "hydra:supportedClass",
    "hydra:title",
    "hydra:entrypoint"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.hydra.APIDocumentation
