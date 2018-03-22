from EPOS import Node

class Person(Node):

  REQUIRED = [
    "dct:identifier"
  ]

  ALLOWED = REQUIRED + [
    "schema:email",
    "schema:familyName",
    "schema:givenName",
    "schema:nationality",
    "schema:telephone",
    "schema:url",
    "schema:address",
    "schema:qualifications",
    "schema:affiliation",
    "schema:availableLanguage"
  ]

  def __init__(self, *args):
    Node.__init__(self, args) 
    self.type = self.schema.Person
