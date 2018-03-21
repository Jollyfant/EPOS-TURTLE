from EPOS import Node

class Project(Node):

  REQUIRED = [
    "dct:identifier",
    "dct:title"
  ]

  ALLOWED = REQUIRED + [
    "dct:description"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.foaf.Project
