from EPOS import Node

class Equipment(Node):

  REQUIRED = [
    "dct:identifier",
    "dct:description",
    "dct:title"
  ]

  ALLOWED = REQUIRED + [
    "dct:type",
    "schema:serialNumber",
    "epos:dynamicRange",
    "epos:filter",
    "epos:orientation",
    "epos:resolution",
    "epos:samplePeriod"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.epos.Equipment
