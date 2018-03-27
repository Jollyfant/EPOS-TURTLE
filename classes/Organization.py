from EPOS import Node

class Organization(Node):

  def __init__(self, *args):
    self.type = self.schema.Organization
    Node.__init__(self, args) 
