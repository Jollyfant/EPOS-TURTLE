from EPOS import Node

class MediaTypeOrExtent(Node):

  REQUIRED = [
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.dct.MediaTypeOrExtent
