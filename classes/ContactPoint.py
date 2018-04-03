from EPOS import Node

class ContactPoint(Node):

  def __init__(self, *args): 
    self.type = self.schema.ContactPoint
    Node.__init__(self, args) 
