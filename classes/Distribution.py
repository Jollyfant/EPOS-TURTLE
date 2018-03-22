from EPOS import Node

class Distribution(Node):

  REQUIRED = [
  ]

  ALLOWED = REQUIRED + [
    "dct:conformsTo"
  ]

  def __init__(self, *args):
    Node.__init__(self, args) 
    self.type = self.dcat.Distribution
