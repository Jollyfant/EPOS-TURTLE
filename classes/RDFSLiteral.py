from EPOS import Node

class RDFSLiteral(Node):

  REQUIRED = [
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.dct.RDFSLiteral
