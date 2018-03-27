from EPOS import Node

class Concept(Node):

  def __init__(self, *args):
    self.type = self.skos.Concept
    Node.__init__(self, args)
