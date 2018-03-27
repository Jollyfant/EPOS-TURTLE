from EPOS import Node

class EPOSWebService(Node):

  def __init__(self, *args): 
    self.type = self.epos.WebService
    Node.__init__(self, args) 
