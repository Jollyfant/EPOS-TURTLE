from EPOS import Node

class PostalAddress(Node):

  def __init__(self, *args):
    self.type = self.schema.PostalAddress
    Node.__init__(self, args)
