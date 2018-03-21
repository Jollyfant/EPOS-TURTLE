from classes.EPOS import EPOSRDF
from classes import *

if __name__ == "__main__":

  """
  
  Example of mapping a Python dict with EPOSRDF classes to TURTLE.
  The supported classes can be found under ./classes/
  
  Author: Mathijs Koymans, 2018
  Copyright: ORFEUS Data Center
  All Rights Reversed.

  Licensed under MIT.

  """

  R = EPOSRDF()
  KNMI_ORG = Organization({"dct:identifier": "PIC:997012076"})

  a = Organization({
    "dct:identifier": "PIC:999518944",
    "schema:url": "http://www.knmi.nl",
    "schema:logo": "http://cdn.knmi.nl/assets/logo_large-1f424789387493844838423432492387342734.png",
    "schema:memberOf": KNMI_ORG,
    "schema:identifier": PropertyValue({
      "schema:propertyID": "PIC",
      "schema:value": "999518944",
    }),
    "schema:address": PostalAddress({
      "schema:streetAddress": "Utrechtseweg, 297",
      "schema:addressLocality": "De Bilt",
      "schema:postalCode": "3731GA",
      "schema:addressCountry": "The Netherlands"
    }),
    "epos:financialContact": Person({"dct:identifier": "http://orcid.org/0000-0001-7750-7254"}),
    "epos:scientificContact": Person({"dct:identifier": "http://orcid.org/0000-0001-7750-7254"}),
    "epos:legalContact": Person({"dct:identifier": "http://orcid.org/0000-0001-7750-7254"}),
    "schema:memberOf": KNMI_ORG 
  })
  
  R.register(a)

  b = EPOSWebService({
    "dct:identifier": "orfeus-eu.org/fdsnws/dataselect/1/",
    "schema:identifier": [
      "orfeus-eu.org/fdsnws/dataselect/1/",
      PropertyValue({
        "schema:propertyID": "DDSS-ID",
        "schema:value": "WP8-DDSS-001",
      }),
    ],
    "schema:description": "Blabla",
    "schema:name": "blabla2",
    "dcat:contactPoint": ContactPoint({"dct:identifier": "http://orcid.org/0000-0001-7750-7254/contactPoint"}),
    "schema:keywords": ["one", "two", "three"],
    "hydra:supportedOperation": HydraOperation({"dct:identifier": "orfeus-eu.org/fdsnws/dataselect/1/query"})
  })

  c = HydraOperation({
    "dct:identifier": "orfeus-eu.org/fdsnws/dataselect/1/query",
    "hydra:method": "GET", 
    "hydra:returns": "binary",
    "hydra:IriTemplate": HydraIriTemplate({
      "hydra:template": "Somestring",
      "hydra:mapping": [
        HydraIriTemplateMapping({
          "hydra:variable": "network",
          "hydra:required": False
        }),
        HydraIriTemplateMapping({
          "hydra:variable": "endtime",
          "hydra:required": False
        }),
        HydraIriTemplateMapping({
          "hydra:variable": "station",
          "hydra:required": False
        })
      ]
    }) 
  })

  d = Person({
    "dct:identifier": "orcid:something",
    "schema:familyName": "Koymans",
    "schema:givenName": "Mathijs",
    "schema:address": PostalAddress({
      "schema:streetAddress": "Thuis!"
    }),
    "schema:qualifications": ["Many", "things"],
    "schema:affiliation": Organization({"dct:identifier": "PIC:999518944"})
  })

  e = ConceptScheme({
    "dct:identifier": "Seismology",
    "dct:title": "Seismology",
    "dct:description": "It contains the concepts of the Seismology domain"
  })

  R.register(b)
  R.register(c)
  R.register(d)
  R.register(e)
  
  print R
