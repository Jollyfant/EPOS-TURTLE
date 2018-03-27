from EPOS import Node

class Document(Node):

  def __init__(self, *args): 
    self.type = self.foaf.Document
    Node.__init__(self, args)
