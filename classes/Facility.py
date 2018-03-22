from EPOS import Node

class Facility(Node):

  REQUIRED = [
    "dct:identifier",
    "dct:description",
    "dct:title"
  ]

  ALLOWED = REQUIRED + [
    "dct:type",
    "foaf:page",
    "vcard:hasAddress"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.epos.Facility
