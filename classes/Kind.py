from EPOS import Node

class Kind(Node):

  def __init__(self, *args): 
    self.type = self.vcard.Kind
    Node.__init__(self, args) 
