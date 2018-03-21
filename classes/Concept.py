from EPOS import Node

class Concept(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "dct:description",
    "skos:inScheme",
    "skos:prefLabel"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.skos.Concept
