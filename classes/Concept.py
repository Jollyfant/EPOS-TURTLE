from EPOS import Node

class Concept(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "dct:description",
    "skos:inScheme",
    "skos:prefLabel",
    "skos:hiddenLabel",
    "skos:altLabel"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.skos.Concept
