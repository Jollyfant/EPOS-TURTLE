from EPOS import Node

class Identifier(Node):

  REQUIRED = [
    "skos:notation"
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.dct.Identifier
