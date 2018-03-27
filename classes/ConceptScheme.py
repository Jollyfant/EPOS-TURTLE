from EPOS import Node

class ConceptScheme(Node):

  def __init__(self, *args): 
    self.type = self.skos.ConceptScheme
    Node.__init__(self, args) 
