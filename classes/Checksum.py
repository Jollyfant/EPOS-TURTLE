from EPOS import Node

class Checksum(Node):

  REQUIRED = [
    "spdx:algorithm",
    "spdx:checksumValue"
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.spdx.Checksum
