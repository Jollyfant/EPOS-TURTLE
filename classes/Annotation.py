from EPOS import Node

class Annotation(Node):

  def __init__(self, *args): 
    self.type = self.oa.Annotation
    Node.__init__(self, args) 
