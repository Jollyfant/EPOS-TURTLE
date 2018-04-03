import json
import os

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
  dct = DCTERMS
  dc = DC
  xsd = XSD
  skos = SKOS
  owl = OWL

  # Define custom namespaces
  adms = Namespace("http://www.w3.org/ns/adms#")
  cnt = Namespace("http://www.w3.org/2011/content#")
  dash = Namespace("http://datashapes.org/dash#")
  dcat = Namespace("http://www.w3.org/ns/dcat#")
  epos = Namespace("http://www.epos-eu.org/epos/dcat-ap#")
  hydra = Namespace("http://www.w3.org/ns/hydra/core#")
  locn = Namespace("http://www.w3.org/ns/locn#")
  oa = Namespace("http://www.w3.org/ns/oa#")
  org = Namespace("http://www.w3.org/ns/org#")
  prov = Namespace("http://www.w3.org/ns/prov#")
  schema = Namespace("http://schema.org/")
  sh = Namespace("http://www.w3.org/ns/shacl#")
  spdx = Namespace("http://spdx.org/rdf/terms#")
  skosxl = Namespace("http://w3.org/2008/05/skos-xl#")
  tosh = Namespace("http://topbraid.org/tosh#")
  vann = Namespace("http://purl.org/vocab/vann/")
  vcard = Namespace("http://www.w3.org/2006/vcard/ns#")
  voaf = Namespace("http://purl.org/vocommons/voaf#")
  wot = Namespace("http://xmlns.com/wot/0.1")

  def __init__(self):
    pass

  def mapPredicate(self, predicate):

    """
    EPOSRDF.mapPredicate
    Maps predicate string ns:field to rdflib class
    """

    # Check if namespace is defined
    if ":" not in predicate:
      raise ValueError("No namespace defined for property: %s in %s" % (predicate, self.__class__.__name__))

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

    # Bind the namespaces to the graph
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
    self.graph.bind("dc", self.dcat)
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
    if isinstance(value, Literal):
      return self.registerNode(identifier, predicate, value)

    # Register a reference or blank node
    if value.identifier is not None:
      return self.registerNode(identifier, predicate, value.identifier)
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

  def registerNode(self, identifier, predicate, value):

    """
    EPOSRDF.registerLiteral
    Registers a string literal to the identifier
    """

    self.addTuple(identifier, predicate, value)

  def serialize(self, format="turtle"):

    """
    EPOSRDF.__str__
    Overload printing operator 
    """

    return self.graph.serialize(format=format)


class RDFValidator(RDFNamespaces):

  """
  Class RDFValidator
  Validates the RDF structures
  """

  SHAPEFILE = os.path.join("shacl", "shapes.ttl")

  def __init__(self):

    """
    EPOSRDF.__init__
    Parses shapes file for simple validation
    """

    # Create a shape
    self.shapes = Graph()
    self.shapes.parse(self.SHAPEFILE, format="turtle")

    shackles = dict()

    # Get all the node shapes
    for s, p, o in self.shapes.triples((None, self.rdf.type, self.sh.NodeShape)):

      namespace = self.shapes.value(s, self.sh.targetClass)

      if namespace is None:
        continue

      shackles[namespace.n3()] = dict()

      # Extract all properties from the shape definition
      for s, p, o in self.shapes.triples((s, self.sh.property, None)):

        allowed = self.getAllowed(o)

        # Property-properties (e.g. min, max)
        path = self.shapes.value(o, self.sh.path)
        minC = self.shapes.value(o, self.sh.minCount) or 0
        maxC = self.shapes.value(o, self.sh.maxCount) or 0

        # Make sure to include shacl.or statements
        orPredicate = self.shapes.value(o, self.sh["or"])
        if orPredicate is not None:
          allowed = allowed + self.extractOr(orPredicate)

        # Remove all None values
        allowed = map(lambda x: x.n3(), filter(lambda x: x is not None, allowed))

        shackles[namespace.n3()][path.n3()] = {
          "minItems": int(minC),
          "maxItems": int(maxC),
          "allowed": allowed,
          "path": path
        }

    self.shackles = shackles

  def extractOr(self, orNode):

    """
    EPOSRDF.extractOr
    Recursively extracts information from shacl:or
    """

    things = list()

    # Get the "first" attribute
    for s, p, o in self.shapes.triples((orNode, self.rdf.first, None)):
      things = things + self.getAllowed(o)

    # Recursion for shacl:rest
    for s, p, o in self.shapes.triples((orNode, self.rdf.rest, None)):
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

    # Convert dictionary literal types
    if dictionary is not None:

      for item in dictionary:

        value = dictionary.get(item)

        # Convert to literal of appropriate type
        if isinstance(value, str) or isinstance(value, unicode):

          # Map URI (URLs)
          if value.startswith("http://") or value.startswith("https://"):
            dictionary[item] = Literal(value, datatype=self.xsd.anyURI)
          else:
            dictionary[item] = Literal(value, datatype=self.xsd.string)

        elif isinstance(value, int):
          dictionary[item] = Literal(value, datatype=self.xsd.integer)
        elif isinstance(value, float):
          dictionary[item] = Literal(value, datatype=self.xsd.float)
        elif isinstance(value, bool):
          dictionary[item] = Literal(value, datatype=self.xsd.boolean)

        # Map datetime to custom EPOS definition
        elif isinstance(value, datetime):
          dictionary[item] = Literal(value, datatype=self.epos.DateOrDateTimeDataType)

      # Sanity checking for the passed dictionary 
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
    Checks the validity of the dictionary
    """

    # Convert keys to rdflib predicates
    predicates = map(lambda x: x.n3(), map(self.mapPredicate, dictionary.keys()))

    # If a shacl:NodeShape was constrained
    if self.type.n3() in self.validator.shackles:

      # Check required
      for n in self.validator.shackles[self.type.n3()]:
        if self.validator.shackles[self.type.n3()][n]["minItems"] > 0:
          if not n in predicates:
            raise ValueError("Attribute %s in %s is required by EPOS RDF" % (n, self.__class__.__name__))

      # Check allowed
      for p in predicates:
        if p not in self.validator.shackles[self.type.n3()]:
          raise ValueError("Attribute %s in %s is not supported by EPOS RDF" % (p, self.__class__.__name__))

      # Check the types
      for p in dictionary:

        if self.mapPredicate(p).n3() in self.validator.shackles[self.type.n3()]:
          allowed = self.validator.shackles[self.type.n3()][self.mapPredicate(p).n3()]["allowed"]

          if isinstance(dictionary[p], Literal):
            if URIRef(dictionary[p].datatype).n3() not in allowed:
              raise ValueError("Attribute %s of type %s in %s is not supported by EPOS RDF. Expected %s" % (p, dictionary[p].datatype, self.__class__.__name__, allowed))

          # Skip all dicts
          elif isinstance(dictionary[p], dict):
            pass

          else:
            if URIRef(dictionary[p].type).n3() not in allowed: 
              raise ValueError("Attribute %s of type %s in %s is not supported by EPOS RDF. Expected %s" % (p, dictionary[p].type, self.__class__.__name__, allowed))

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

    if isinstance(argument, str) or isinstance(argument, unicode):
      return argument, None

    # Arguments are invalid
    raise ValueError("EPOS Class %s called with invalid parameters" % self.__class__.__name__)
