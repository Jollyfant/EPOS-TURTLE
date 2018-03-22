# EPOS-TURTLE 🐢

Python library for EPOS-RDF conversion.

## Dependencies

* Python [RDFLib](https://rdflib.readthedocs.io/en/stable/)

## Example Usage

    from classes.EPOS import EPOSRDF
    from classes import *

    R = EPOSRDF()

    Org = Organization("PIC:997012076", {
      "epos:legalContact": Person("http://orcid.org/0000-0001-7750-7254")
    })

    R.register(Org)

    print R

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
