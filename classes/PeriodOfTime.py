from EPOS import Node

class PeriodOfTime(Node):

  REQUIRED = [
  ]

  ALLOWED = REQUIRED + [
    "schema:endDate",
    "schema:startDate"
  ]

  def __init__(self, identifier, dictionary):
    Node.__init__(self, identifier, dictionary)
    self.type = self.dct.PeriodOfTime
