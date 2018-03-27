from EPOS import Node

class Dataset(Node):

  def __init__(self, *args): 
    self.type = self.dcat.Dataset
    Node.__init__(self, args)
