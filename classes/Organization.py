from EPOS import Node

class Organization(Node):

  ALLOWED = [
    "dct:identifier",
    "schema:url",
    "schema:legalName",
    "schema:logo",
    "schema:memberOf",
    "schema:identifier",
    "schema:address",
    "epos:financialContact",
    "epos:scientificContact",
    "epos:legalContact",
    "schema:memberOf"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.schema.Organization
