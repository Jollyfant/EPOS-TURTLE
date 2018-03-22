from EPOS import Node

class ContactPoint(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "schema:email",
    "schema:availableLanguage"
  ]

  def __init__(self, *args): 
    Node.__init__(self, args) 
    self.type = self.schema.ContactPoint
