from EPOS import Node

class Distribution(Node):

  def __init__(self, *args):
    self.type = self.dcat.Distribution
    Node.__init__(self, args) 
