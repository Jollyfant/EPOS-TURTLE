from EPOS import Node

class PostalAddress(Node):

  ALLOWED = [
    "schema:streetAddress",
    "schema:addressLocality",
    "schema:postalCode",
    "schema:addressCountry"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, None, dictionary)
    self.type = self.schema.PostalAddress
