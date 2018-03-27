from EPOS import Node

class Project(Node):

  def __init__(self, *args): 
    self.type = self.foaf.Project
    Node.__init__(self, args) 
