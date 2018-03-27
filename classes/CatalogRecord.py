from EPOS import Node

class CatalogRecord(Node):

  def __init__(self, *args): 
    self.type = self.dcat.CatalogRecord
    Node.__init__(self, args) 
