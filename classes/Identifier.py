from EPOS import Node

class Identifier(Node):

  REQUIRED = [
    "skos:notation"
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.dct.Identifier
