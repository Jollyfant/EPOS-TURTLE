from EPOS import Node

class Dataset(Node):

  REQUIRED = [
    "dct:identifier",
    "dct:description",
    "dct:title"
  ]

  ALLOWED = REQUIRED + [
    "cnt:characterEncoding",
    "dct:relation",
    "dct:source",
    "dct:hasPart",
    "schema:keywords",
    "dct:contactPoint",
    "dct:temporal",
    "dct:provenance",
    "dct:accessRights",
    "dct:conformsTo",
    "dcat:distribution",
    "dct:publisher",
    "dct:type",
    "dct:subject",
    "dct:created",
    "adms:versionNotes",
    "adms:identifier",
    "dct:issued",
    "owl:versionInfo",
    "dct:accrualPeriodicity",
    "foaf:page",
    "dct:landingPage",
    "dct:spatial",
    "dct:isPartOf",
    "dct:isVersionOf",
    "dct:language"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.dcat.Dataset
