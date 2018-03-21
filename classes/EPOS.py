from datetime import datetime
from rdflib import URIRef, Literal, Graph, BNode
from rdflib.namespace import FOAF, RDF, RDFS, DCTERMS, DC, XSD, SKOS
from rdflib import Namespace

class EPOSRDF():

  """
  Class EPOSRDF
  Master class for EPOS RDF
  """

  # Define EPOS-RDF Namespaces
  rdf = RDF
  rdfs = RDFS
  foaf = FOAF
  dcat = DCTERMS
  dct = DC
  xsd = XSD
  skos = SKOS

  owl = Namespace("http://www.w3.org/2002/07/owl#")
  adms = Namespace("http://www.w3.org/ns/adms#")
  oa = Namespace("http://www.w3.org/ns/oa#")
  vcard = Namespace("http://www.w3.org/2006/vcard/ns#")
  cnt = Namespace("http://www.w3.org/2011/content#")
  locn = Namespace("http://www.w3.org/ns/locn#")
  hydra = Namespace("http://www.w3.org/ns/hydra/core#")
  epos = Namespace("http://www.epos-eu.org/epos/dcat-ap#")
  schema = Namespace("http://schema.org/")

  def __init__(self):

    # Create graph
    self.graph = Graph()

    # Bind the namespaces
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


  def mapPredicate(self, predicate):

    """
    EPOSRDF.mapPredicate
    Maps predicate string ns:field to rdflib class
    """

    (namespace, item) = predicate.split(":")
    return getattr(self, namespace)[item]


  def register(self, element):

    """
    EPOSRDF.register
    Register an entity with rdflib
    """

    # Identifier is the dct:identifier
    identifier = element.identifier

    # Add the identifier under the correct namespace
    if identifier is not None:
      self.graph.add((identifier, self.rdf.type, element.type))

    # Go over all keys in the dictionary
    for key in element.dictionary:

      # Skip the dct:identifier internal attribute
      if key == "dct:identifier":
        continue

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


  def __str__(self):

    """
    EPOSRDF.__str__
    Overload printing operator 
    """

    return self.graph.serialize(format='turtle')


class Node(EPOSRDF):

  """
  Class Node
  Parent for all EPOS-RDF classes
  """

  def __init__(self, dictionary):

    # Sanity checking for required
    if hasattr(self, "REQUIRED"):
      for required in self.REQUIRED:
        if required not in dictionary:
          raise ValueError("Attribute %s in %s is required by EPOS RDF" % (required, self.__class__.__name__))

    # Sanity checking for allowed
    for item in dictionary:
      if item not in self.ALLOWED:
        raise ValueError("Attribute %s in %s is not supported by EPOS RDF" % (item, self.__class__.__name__))

    # Set the dictionary items
    self.dictionary = dictionary

    # Get and set the URIRef identifier
    value = dictionary.get("dct:identifier")

    if value is not None:
      self.identifier = URIRef(value)
    else:
      self.identifier = None
