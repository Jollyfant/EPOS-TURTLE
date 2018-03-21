from EPOS import Node

class EPOSWebService(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "dct:issued",
    "dct:modified",
    "schema:provider",
    "schema:identifier",
    "schema:name",
    "schema:description",
    "schema:keywords",
    "dcat:contactPoint",
    "dcat:theme",
    "hydra:supportedOperation",
    "hydra:entrypoint"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.epos.WebService
