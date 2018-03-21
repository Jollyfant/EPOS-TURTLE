from EPOS import Node

class SoftwareApplication(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.schema.SoftwareApplication
