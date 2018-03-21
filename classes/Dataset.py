from EPOS import Node

class Dataset(Node):

  REQUIRED = [
    "dct:identifier",
    "dct:description",
    "dct:title"
  ]

  ALLOWED = REQUIRED + [
    "dct:type",
    "dct:subject",
    "dct:created",
    "adms:versionNotes",
    "dct:issued",
    "owl:versionInfo"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.dcat.Dataset
