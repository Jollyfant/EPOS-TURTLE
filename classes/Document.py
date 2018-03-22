from EPOS import Node

class Document(Node):

  REQUIRED = [
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.foaf.Document
