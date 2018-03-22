from EPOS import Node

class Agent(Node):

  REQUIRED = [
    "foaf:name"
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.foaf.Agent