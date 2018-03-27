from EPOS import Node

class MediaTypeOrExtent(Node):

  def __init__(self, *args): 
    self.type = self.dct.MediaTypeOrExtent
    Node.__init__(self, args) 
