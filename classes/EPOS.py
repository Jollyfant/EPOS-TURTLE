import json
from datetime import datetime
from rdflib.serializer import Serializer
from rdflib import URIRef, Literal, Graph, BNode
from rdflib.namespace import FOAF, RDF, RDFS, DCTERMS, DC, XSD, SKOS, OWL
from rdflib import Namespace

class RDFNamespaces():

  """
  Class RDFNamespaces
  Holds namespaces for EPOSRDF
  """

  rdf = RDF
  rdfs = RDFS
  foaf = FOAF
  dcat = DCTERMS
  dct = DC
  xsd = XSD
  skos = SKOS
  owl = OWL

  # Define custom namespaces
  sh = Namespace("http://www.w3.org/ns/shacl#")
  spdx = Namespace("http://spdx.org/rdf/terms#")
  adms = Namespace("http://www.w3.org/ns/adms#")
  oa = Namespace("http://www.w3.org/ns/oa#")
  vcard = Namespace("http://www.w3.org/2006/vcard/ns#")
  cnt = Namespace("http://www.w3.org/2011/content#")
  locn = Namespace("http://www.w3.org/ns/locn#")
  hydra = Namespace("http://www.w3.org/ns/hydra/core#")
  epos = Namespace("http://www.epos-eu.org/epos/dcat-ap#")
  schema = Namespace("http://schema.org/")

  def __init__(self):
    pass

  def mapPredicate(self, predicate):

    """
    EPOSRDF.mapPredicate
    Maps predicate string ns:field to rdflib class
    """

    (namespace, item) = predicate.split(":")
    return getattr(self, namespace)[item]


class EPOSRDF(RDFNamespaces):

  """
  Class EPOSRDF
  Master class for EPOS RDF
  """

  def __init__(self):

    """
    EPOSRDF.__init__
    Initializes EPOSRDF class
    """

    # Create graph
    self.graph = Graph()

    # Bind the namespaces
    self.graph.bind("sh", self.sh)
    self.graph.bind("spdx", self.spdx)
    self.graph.bind("skos", self.skos)
    self.graph.bind("adms", self.adms)
    self.graph.bind("owl", self.owl)
    self.graph.bind("rdfs", self.rdfs)
    self.graph.bind("cnt", self.cnt)
    self.graph.bind("schema", self.schema)
    self.graph.bind("oa", self.oa)
    self.graph.bind("epos", self.epos)
    self.graph.bind("hydra", self.hydra)
    self.graph.bind("locn", self.locn)
    self.graph.bind("dcat", self.dcat)
    self.graph.bind("dct", self.dct)
    self.graph.bind("vcard", self.vcard)


  def addTuple(self, subject, predicate, object):

    """
    EPOSRDF.addTuple
    Maps predicate string ns:field to rdflib class
    """

    self.graph.add((subject, predicate, object))

  def register(self, element):

    """
    EPOSRDF.register
    Register an entity with rdflib
    """

    # Identifier is the dct:identifier
    identifier = element.identifier

    # Add the identifier under the correct namespace
    if identifier is not None:
      self.addTuple(identifier, self.rdf.type, element.type)

    if element.dictionary is None:
      return

    # Go over all keys in the dictionary
    for key in element.dictionary:

      # Get the value
      value = element.dictionary.get(key)

      # Splat to list
      if not isinstance(value, list):
        value = [value]

      # Register all elements in the list
      for i in value:
        self.registerElement(identifier, key, i)

  def registerElement(self, identifier, key, value):

    """
    EPOSRDF.registerElement
    Registers an element to rdflib
    """

    # Get the rdflib predicate from the key
    predicate = self.mapPredicate(key)

    # Register literals 
    if isinstance(value, str):
      return self.registerLiteral(identifier, predicate, value, self.xsd.string)
    elif isinstance(value, bool):
      return self.registerLiteral(identifier, predicate, value, self.xsd.boolean)
    elif isinstance(value, int):
      return self.registerLiteral(identifier, predicate, value, self.xsd.integer)
    elif isinstance(value, float):
      return self.registerLiteral(identifier, predicate, value, self.xsd.float)
    elif isinstance(value, datetime):
      return self.registerLiteral(identifier, predicate, value, self.xsd.datetime)

    # Register a reference or blank node
    if value.identifier is not None:
      return self.registerReference(identifier, predicate, value.identifier)
    else:
      return self.registerBlankNode(identifier, predicate, value)

  def registerBlankNode(self, reference, predicate, value):

    """
    EPOSRDF.registerBlankNode
    Registers a blank node
    """

    # Create a new node: overwrite the identifier
    value.identifier = BNode()

    # Recursion for nested Objects
    self.register(value)

    # Add the node itself the graph
    self.addTuple(reference, predicate, value.identifier)


  def registerReference(self, identifier, predicate, reference):

    """
    EPOSRDF.registerLiteral
    Registers a string literal to the identifier
    """

    self.addTuple(identifier, predicate, reference)


  def registerLiteral(self, identifier, predicate, value, datatype):

    """
    EPOSRDF.registerLiteral
    Registers a string literal to the identifier
    """

    self.addTuple(identifier, predicate, Literal(value, datatype=datatype))

  """
  def __str__(self):

    EPOSRDF.__str__
    Overload printing operator 

    return self.graph.serialize(format="turtle")
  """


class RDFValidator(RDFNamespaces):

  def __init__(self):

    """
    EPOSRDF.__init__
    Parses shapes file for simple validation
    """

    # Create a shape
    self.shapes = Graph()
    self.shapes.parse("shapes.ttl", format="turtle")

    collection = dict()

    # Get all the node shapes
    for s, p, o in self.shapes.triples((None, self.rdf.type, self.sh.NodeShape)):

      namespace = self.shapes.value(s, self.sh.targetClass)

      if namespace is None:
        continue

      collection[namespace.n3()] = dict()

      for s, p, o in self.shapes.triples((s, self.sh.property, None)):

        allowed = self.getAllowed(o)

        path = self.shapes.value(o, self.sh.path)
        minC = self.shapes.value(o, self.sh.minCount) or 0
        maxC = self.shapes.value(o, self.sh.maxCount) or 0

        # Make sure to include shacl.or statements
        orPredicate = self.shapes.value(o, self.sh["or"])
        if orPredicate is not None:
          allowed = allowed + self.extractOr(orPredicate)

        # Remove all None values
        allowed = filter(lambda x: x is not None, allowed)

        collection[namespace.n3()][path.n3()] = {
          "minItems": int(minC),
          "maxItems": int(maxC),
          "allowed": allowed
        }

    self.collection = collection
    print self.collection

  def extractOr(self, o):

    """
    EPOSRDF.extractOr
    Recursively extracts information from shacl:or
    """

    things = list()

    # Get the "first" attribute
    for s, p, o in self.shapes.triples((o, self.rdf.first, None)):
      things = things + self.getAllowed(o)

    # Recursion for shacl:rest
    for s, p, o in self.shapes.triples((o, self.rdf.rest, None)):
      things = things + self.extractOr(o)

    return things

  def getAllowed(self, o):

    """
    EPOSRDF.getAllowed
    Gets the allowed types for a node
    """

    nodes = list()

    # Supported shacl types
    for thing in ["datatype", "class", "nodeKind", "node"]:
      nodes.append(self.shapes.value(o, self.sh[thing]))

    return nodes

class Node(RDFNamespaces):

  """
  Class Node
  Parent for all EPOS-RDF classes
  """

  # Create a validator for all nodes
  validator = RDFValidator()

  def __init__(self, args):

    """
    Node.__init__
    Initializes a new node
    """
   
    identifier, dictionary = self.parseArguments(args)

    # Sanity checking for required
    if dictionary is not None:
      self.checkDictionary(dictionary)

    # Set the dictionary items
    self.dictionary = dictionary

    if identifier is not None:
      self.identifier = URIRef(identifier)
    else:
      self.identifier = None


  def checkDictionary(self, dictionary):

    """
    Node.checkDictionary
    """

    if hasattr(self, "REQUIRED"):
      for required in self.REQUIRED:
        if required not in dictionary:
          raise ValueError("Attribute %s in %s is required by EPOS RDF" % (required, self.__class__.__name__))

    # Sanity checking for allowed
    for item in dictionary:
      if item not in self.ALLOWED:
        raise ValueError("Attribute %s in %s is not supported by EPOS RDF" % (item, self.__class__.__name__))


  def parseArguments(self, arguments):

    """
    Node.parseArguments
    Parses the arguments: (identifier), (dict), (identifier, dict)
    """

    # No arguments
    if len(arguments) == 0:
      raise ValueError("EPOS Class %s called without parameters" % self.__class__.__name__)

    # Identifier & dictionary specified
    if len(arguments) == 2:
      return arguments

    # Single argument: determine which
    argument = arguments[0]

    if isinstance(argument, dict):
      return None, argument

    if isinstance(argument, str):
      return argument, None

    # Arguments are invalid
    raise ValueError("EPOS Class %s called with invalid parameters" % self.__class__.__name__)
