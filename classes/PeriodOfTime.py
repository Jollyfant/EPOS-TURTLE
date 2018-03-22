from EPOS import Node

class PeriodOfTime(Node):

  REQUIRED = [
  ]

  ALLOWED = REQUIRED + [
    "schema:endDate",
    "schema:startDate"
  ]

  def __init__(self, dictionary):
    Node.__init__(self, dictionary)
    self.type = self.dct.PeriodOfTime
