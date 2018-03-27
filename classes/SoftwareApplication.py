from EPOS import Node

class SoftwareApplication(Node):

  def __init__(self, *args): 
    self.type = self.schema.SoftwareApplication
    Node.__init__(self, args)
