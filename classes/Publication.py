from EPOS import Node

class Publication(Node):

  REQUIRED = [
    "dct:identifier",
    "dct:title"
  ]

  ALLOWED = REQUIRED + [
    "dct:abstract",
    "dct:issued",
    "schema:issn",
    "schema:numberOfPages",
    "schema:volumeNumber"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.epos.Publication
