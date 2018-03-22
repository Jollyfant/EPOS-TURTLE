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

  def __init__(self, *args): 
    Node.__init__(self, args) 
    self.type = self.epos.WebService
