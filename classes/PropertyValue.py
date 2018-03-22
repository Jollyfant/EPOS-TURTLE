from EPOS import Node

class PropertyValue(Node):

  ALLOWED = [
    "schema:propertyID",
    "schema:value"
  ]

  def __init__(self, *args): 
    Node.__init__(self, args) 
    self.type = self.schema.PropertyValue
