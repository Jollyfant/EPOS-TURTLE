from EPOS import Node

class ConceptScheme(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "dct:title",
    "dct:description"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.skos.ConceptScheme
