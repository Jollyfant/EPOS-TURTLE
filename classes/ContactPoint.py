from EPOS import Node

class ContactPoint(Node):

  def __init__(self, *args): 
    self.type = self.epos.ContactPointType
    Node.__init__(self, args) 
