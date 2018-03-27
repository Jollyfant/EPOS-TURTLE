from EPOS import Node

class Agent(Node):

  def __init__(self, *args): 
    self.type = self.foaf.Agent
    Node.__init__(self, args)
