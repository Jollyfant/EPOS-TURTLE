from EPOS import Node

class Service(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "schema:description",
    "schema:name",
    "schema:serviceType"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.schema.Service
