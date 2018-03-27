from EPOS import Node

class Resource(Node):

  def __init__(self, *args): 
    self.type = self.rdfs.Resource
    Node.__init__(self, args) 
