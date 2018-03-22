from EPOS import Node

class Project(Node):

  REQUIRED = [
    "dct:identifier",
    "dct:title"
  ]

  ALLOWED = REQUIRED + [
    "dct:description"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.foaf.Project
