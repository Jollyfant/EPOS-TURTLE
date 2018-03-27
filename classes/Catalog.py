from EPOS import Node

class Catalog(Node):

  def __init__(self, *args): 
    self.type = self.dcat.Catalog
    Node.__init__(self, args) 
