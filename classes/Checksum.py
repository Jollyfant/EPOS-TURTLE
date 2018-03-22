from EPOS import Node

class Checksum(Node):

  REQUIRED = [
    "spdx:algorithm",
    "spdx:checksumValue"
  ]

  ALLOWED = REQUIRED + [
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.spdx.Checksum
