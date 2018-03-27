from EPOS import Node

class Person(Node):

  def __init__(self, *args):
    self.type = self.schema.Person
    Node.__init__(self, args) 
