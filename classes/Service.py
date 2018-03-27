from EPOS import Node

class Service(Node):

  def __init__(self, *args): 
    self.type = self.schema.Service
    Node.__init__(self, args) 
