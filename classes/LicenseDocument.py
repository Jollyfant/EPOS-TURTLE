from EPOS import Node

class LicenseDocument(Node):

  def __init__(self, *args): 
    self.type = self.dct.LicenseDocument
    Node.__init__(self, args) 
