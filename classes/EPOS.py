from datetime import datetime
from rdflib import URIRef, Literal, Graph, BNode
from rdflib.namespace import FOAF, RDF, RDFS, DCTERMS, DC, XSD, SKOS
from rdflib import Namespace

class EPOSRDF():

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

  def mapPredicate(self, predicate):

    (namespace, item) = predicate.split(":")
    return getattr(self, namespace)[item]


  def register(self, element):

    identifier = element.identifier

    # When no identifier is given: add to graph
    if identifier is not None:
      self.graph.add((identifier, self.rdf.type, element.type))

    for key in element.items:

      # Skip the dct:identifier internal attribute
      if key == "dct:identifier":
        continue

      # Get the value
      value = element.items.get(key)

      # Splat to list
      if not isinstance(value, list):
        value = [value]

      for i in value:
        self.registerElement(identifier, key, i)

  def registerElement(self, identifier, key, value):

    # Register literals 
    if isinstance(value, str):
      self.registerLiteral(identifier, key, value, self.xsd.string)
    elif isinstance(value, bool):
      self.registerLiteral(identifier, key, value, self.xsd.boolean)
    elif isinstance(value, int):
      self.registerLiteral(identifier, key, value, self.xsd.integer)
    elif isinstance(value, float):
      self.registerLiteral(identifier, key, value, self.xsd.float)
    elif isinstance(value, datetime):
      self.registerLiteral(identifier, key, value, self.xsd.datetime)
    else:
      if value.identifier is not None:
        self.registerReference(identifier, key, value.identifier)
      else:
        self.registerNode(identifier, key, value)

  def registerNode(self, reference, key, value):

    # Create a new node: overwrite the identifier
    value.identifier = BNode()

    # Recursion for nested Objects
    self.register(value)

    # Add the node itself the graph
    self.graph.add((reference, self.mapPredicate(key), value.identifier))

  def registerReference(self, identifier, key, reference):
    self.graph.add((identifier, self.mapPredicate(key), reference))

  # Register a literal
  def registerLiteral(self, identifier, key, value, datatype):
    self.graph.add((identifier, self.mapPredicate(key), Literal(value, datatype=datatype)))

  def __str__(self):
    return self.graph.serialize(format="turtle")


class Node(EPOSRDF):

  def __init__(self, dictionary):

    # Sanity checking for required & allowed
    for item in dictionary:

      if hasattr(self, "REQUIRED"):
        for required in self.REQUIRED:
          if required not in dictionary:
            raise ValueError("Attribute %s in %s is required by EPOS RDF" % (required, self.__class__.__name__))

      if item not in self.ALLOWED:
        raise ValueError("Attribute %s in %s is not supported by EPOS RDF" % (item, self.__class__.__name__))

    # Set the dictionary items
    self.items = dictionary

    # Get and set the URIRef identifier
    value = dictionary.get("dct:identifier")

    if value is not None:
      self.identifier = URIRef(value)
    else:
      self.identifier = None
