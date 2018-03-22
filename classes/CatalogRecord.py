from EPOS import Node

class CatalogRecord(Node):

  REQUIRED = [
    "dct:identifier",
    "dct:created",
    "dct:modified",
    "foaf:primaryTopic"
  ]

  ALLOWED = REQUIRED + [
    "dct:source",
    "dct:language",
    "dct:characterEncoding",
    "dct:issued",
    "dct:decsriptiond",
    "dct:title",
    "owl:versionInfo"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.dcat.CatalogRecord
