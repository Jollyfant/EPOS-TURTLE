from EPOS import Node

class PropertyValue(Node):

  ALLOWED = [
    "schema:propertyID",
    "schema:value"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.schema.PropertyValue
