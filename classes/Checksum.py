from EPOS import Node

class Checksum(Node):

  def __init__(self, *args): 
    self.type = self.spdx.Checksum
    Node.__init__(self, args) 
