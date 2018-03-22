from EPOS import Node

class PostalAddress(Node):

  ALLOWED = [
    "schema:streetAddress",
    "schema:addressLocality",
    "schema:postalCode",
    "schema:addressCountry"
  ]

  def __init__(self, *args):
    Node.__init__(self, args)
    self.type = self.schema.PostalAddress
