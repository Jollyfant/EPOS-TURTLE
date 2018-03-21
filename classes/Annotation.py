from EPOS import Node

class Annotation(Node):

  REQUIRED = [
  ]

  ALLOWED = REQUIRED + [
    "dct:created",
    "dct:creator"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.oa.Annotation
