# EPOS-TURTLE 🐢

Python library for EPOS-RDF conversion.

## Dependencies

* Python [RDFLib](https://rdflib.readthedocs.io/en/stable/)

## EPOS-RDF Classes

EPOS-RDF Classes can be called with an identifier, dictionary or both. A class can be registered within the RDF graph using the `.register` method. Multiple classes can be nested in the dictionaries. Input is checked against the shapes contraint file (shacl).

| Call                          | Result     |
| ----------------------------- | ---------- |
| Class(identifier)             | Reference  |
| Class(dictionary)             | Blank Node |
| Class(identifier, dictionary) | Graph Node |

To extract the RDF call the `serialize()` method. The default format is "turtle".

## Python - EPOSRDF Mapping

Python native types are mapped to RDF types using the following conversion table.

| Native Type       | RDF Type                    |
| ----------------- | --------------------------- |
| datetime.datetime | epos.DateOrDateTimeDataType |
| str, unicode      | xsd.string                  |
| boolean           | xsd.boolean                 |
| int               | xsd.integer                 |
| float             | xsd.float                   |
| URI http(s)://    | xsd.anyURI                  |
| list              | Recursive type mapping      |

## Example Usage

    from classes.EPOS import EPOSRDF
    from classes import *

    R = EPOSRDF()

    Org = Organization("PIC:997012076", {
      "epos:legalContact": Person("http://orcid.org/0000-0001-7750-7254"),
      "schema:address": PostalAddress({
        "streetAddress": "Utrechtseweg 279"
      })
    })

    R.register(Org)

    print R.serialize()

Supported EPOS-RDF Classes:

* Agent
* Annotation
* Catalog
* CatalogRecord
* Checksum
* Concept
* ConceptScheme
* ContactPoint
* CreativeWork
* Dataset
* Document
* EPOSWebService
* Equipment
* Facility
* Frequency
* HydraAPIDocumentation
* HydraClass
* HydraIriTemplate
* HydraIriTemplateMapping
* HydraOperation
* Identifier
* Kind
* LicenseDocument
* LinguisticSystem
* Location
* MediaTypeOrExtent
* Organization
* PeriodOfTime
* Person
* PostalAddress
* Project
* PropertyValue
* ProvenanceStatement
* Publication
* RDFSLiteral
* Resource
* RightsStatement
* Service
* SoftwareApplication
* SoftwareSourceCode
* Standard
