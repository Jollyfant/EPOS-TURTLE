from EPOS import Node

class PeriodOfTime(Node):

  def __init__(self, *args): 
    self.type = self.dct.PeriodOfTime
    Node.__init__(self, args) 
