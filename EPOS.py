import datetime
import json

from classes.EPOS import EPOSRDF
from classes import *

if __name__ == "__main__":

  """
  
  See the README for an example.
  
  Author: Mathijs Koymans, 2018
  Copyright: ORFEUS Data Center
  All Rights Reversed.

  Licensed under MIT.

  """

  R = EPOSRDF()

  # Organization example
  Org = Organization("PIC:000000000", {
    "schema:identifier": "organizationIdentifier",
    "schema:legalName": "A name",
    "schema:logo": "http://identifier.id",
    "schema:email": "someone@test.org",
    "dcat:contactPoint": ContactPoint("http://orcid.org/0000-0000-0000-0000"), 
    "epos:scientificContact": Person("http://orcid.org/0000-0000-0000-0000"),
    "epos:legalContact": Person("http://orcid.org/0000-0000-0000-0000"),
    "schema:address": PostalAddress({
      "schema:streetAddress": "A street"
    })
  })

  # Person example
  Pers = Person("http://orcid.org/0000-0000-0000-0000", {
    "schema:identifier": "personIdentifier"
  })

  # Contact point example
  CPoint = ContactPoint("contactPointId", {
    "schema:name": "A name",
    "schema:availableLanguage": "Some languages",
    "schema:telephone": "0000100000"
  })

  Webs = EPOSWebService("webserviceId", {
    "dcat:theme": Concept("ConceptReference"),
    "dct:issued": datetime.datetime.now(), 
    "dct:modified": datetime.datetime.now(),
    "schema:name": "Some description",
    "schema:description": "Some description",
    "schema:provider": Organization("PIC:000000000"), 
    "hydra:entrypoint": "http://www.orfeus-eu.org/fdsnws/station/1/query",
    "dcat:contactPoint": ContactPoint("contactPointId"),
    "schema:identifier": "Some identifier"
  })

  R.register(Org)
  R.register(CPoint)
  R.register(Pers)
  R.register(Webs)
  
  print R.serialize(format="json-ld")
