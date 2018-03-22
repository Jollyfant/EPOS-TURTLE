from EPOS import Node

class Catalog(Node):

  REQUIRED = [
    "dct:description",
    "dct:title",
    "dct:identifier",
    "dct:publisher"
  ]

  ALLOWED = REQUIRED + [
    "dct:issued",
    "foaf:hompage",
    "dct:license",
    "dct:spatial",
    "skos:modified",
    "dcat:record"
    "dct:hasPart",
    "dcat:themeTaxonomy"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.dcat.Catalog
