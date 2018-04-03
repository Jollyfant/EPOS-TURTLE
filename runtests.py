import datetime
import warnings
import unittest
import json

from classes.EPOS import EPOSRDF, Node
from classes import *

class TestStringMethods(unittest.TestCase):

  # Ignore warnings
  warnings.simplefilter("ignore")
  R = EPOSRDF()

  def test_no_namespace(self):

    with self.assertRaises(ValueError) as ctx:
      Organization({
        "namespace": "missing"
      })
    self.assertEqual("No namespace defined for property: namespace in Organization", str(ctx.exception))

  def test_empty_class(self):

    with self.assertRaises(ValueError) as ctx:
      Organization()
    self.assertEqual("EPOS Class Organization called without parameters", str(ctx.exception))

  def test_uri_class(self):

    org = Organization("http://uri-to-whereever")
    self.assertEqual(org.type, self.R.schema.Organization)

  def test_uri_dict(self):

    loc = Location({
      "locn:geometry": "POINT(0 0 0)"
    })

    self.assertEqual(loc.type, self.R.dct.Location)

  def test_organization(self):

    Organization("URI")

     # Required
    with self.assertRaises(ValueError) as ctx:
      Organization({})
    self.assertEqual("Attribute <http://schema.org/identifier> in Organization is required by EPOS RDF", str(ctx.exception))

    # Valid organization
    Organization("URI", {
      "schema:identifier": ["URI", "URI2"],
      "schema:legalName": "legalName",
      "schema:leiCode": "leiCode",
      "epos:annotation": Annotation("URI"),
      "schema:address": "address",
      "schema:logo": "http://logo",
      "schema:url": "http://url",
      "schema:email": "email",
      "schema:telephone": "012345678",
      "dcat:contactPoint": ContactPoint("URI"),
      "schema:memberOf": Organization("URI"),
      "schema:owns": [
        Equipment("URI"),
        Facility("URI-2")
      ]
    })


  def test_person(self):

    # Test person as URI
    Person("URI")

    # Required
    with self.assertRaises(ValueError) as ctx:
      Person({})
    self.assertEqual("Attribute <http://schema.org/identifier> in Person is required by EPOS RDF", str(ctx.exception))

    # Test schema:identifier types string, URI, PropertyValue
    Person({"schema:identifier": "EPOS/Person/abc"})
    Person({"schema:identifier": "http://EPOS/Person/abc"})
    Person({"schema:identifier": PropertyValue("")})

    # Check raises on wrong types
    with self.assertRaises(ValueError) as ctx:
      Person({"schema:identifier": 0})
    with self.assertRaises(ValueError) as ctx:
      Person({"schema:identifier": datetime.datetime.now()})

    # Valid person entity
    Person("URI", {
      "schema:identifier": "URI",
      "schema:familyName": "familyName",
      "schema:givenName": "givenName",
      "dcat:contactPoint": ContactPoint("URI"),
      "schema:address": PostalAddress({
        "schema:postalCountry": "postalCountry"
      }),
      "schema:email": "email",
      "schema:qualifications": "qualifications",
      "schema:telephone": "012345678",
      "schema:url": "http://url",
      "schema:affiliation": Organization("URI"),
      "epos:annotation": Annotation("URI")
    })


if __name__ == "__main__":
  unittest.main()
