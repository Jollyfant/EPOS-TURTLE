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

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.schema.Service
