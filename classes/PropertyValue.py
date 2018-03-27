from EPOS import Node

class PropertyValue(Node):

  def __init__(self, *args): 
    self.type = self.schema.PropertyValue
    Node.__init__(self, args) 
