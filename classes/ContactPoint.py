from EPOS import Node

class ContactPoint(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "schema:email",
    "schema:availableLanguage"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.schema.ContactPoint
