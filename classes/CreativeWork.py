from EPOS import Node

class CreativeWork(Node):

  def __init__(self, *args): 
    self.type = self.schema.CreativeWork
    Node.__init__(self, args) 
