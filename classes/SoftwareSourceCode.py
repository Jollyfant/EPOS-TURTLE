from EPOS import Node

class SoftwareSourceCode(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.schema.SoftwareSourceCode
