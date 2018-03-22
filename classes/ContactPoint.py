from EPOS import Node

class ContactPoint(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "schema:email",
    "schema:availableLanguage"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.schema.ContactPoint
