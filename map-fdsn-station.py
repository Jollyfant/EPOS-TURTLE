import datetime
import requests
import os
import json

from classes.EPOS import EPOSRDF
from classes import *

node = "ODC"
webservice = "https://www.orfeus-eu.org/fdsnws/station/1/query"
prefix = "/EPOS/ORFEUS/EIDA/%s" % node

def getStationInformation(level, network="*", station="*", channel="*"):

  # Create the query string
  qs = webservice + "?" + "&".join([
    "network=%s" % network,
    "station=%s" % station,
    "channel=%s" % channel,
    "level=%s" % level,
    "format=text"
  ])

  return requests.get(qs).text.split("\n")[1:-1]
 
def registerNetworks(network):

  networks = list()

  for line in getStationInformation("network", network=network):

    (network,
     description,
     starttime,
     endttime,
     nStations) = line.split("|")

    networks.append(network)

    eposIdentifier = "%s/%s" % (prefix, network)

    facility = Facility(eposIdentifier, {
      "dct:identifier": eposIdentifier,
      "dct:description": "Seismic Network: %s" % description,
      "dct:title": "Seismic Network",
      "dcat:theme": Concept("SeismicNetwork"),
      "dct:type": "https://orfeus-eu.org/ns/network",
      "dcat:contactPoint": ContactPoint("/EPOS/ORFEUS/EIDA/ODC/MRKOYMANS")
    })

    R.register(facility)

    registerStations(network)

  # Return a list of all network facilities
  return networks

def registerStations(network):

  # Map station to facility
  for line in getStationInformation("station", network=network):

    (network,
     station,
     latitude,
     longitude,
     elevation,
     description,
     starttime,
     endtime) = line.split("|")

    identifier = "%s.%s" % (network, station)
    eposIdentifier = "%s/%s" % (prefix, identifier)

    # Create the station equipment
    equipment = Equipment(eposIdentifier, {
      "dct:identifier": eposIdentifier,
      "dct:description": "Seismic station",
      "dct:type": "https://orfeus-eu.org/ns/station",
      "schema:manufacturer": Organization("/EPOS/ORGANIZATION/KNMI"),
      "dct:title": "Seismic Station for %s" % identifier,
      "dct:spatial": Location({
        "locn:geometry": "POINT(%s %s %s)" % (latitude, longitude, elevation)
      }),
      "schema:serialNumber": identifier,
      "dcat:contactPoint": ContactPoint("/EPOS/ORFEUS/EIDA/ODC/MRKOYMANS")
    })

    R.register(equipment)

    registerChannels(network, station)

def getSampleRate(sampleRate):

  try:
    return str(1000 / float(sampleRate))
  except Exception:
    return "0"

def registerChannels(network, station):

  # Map stream to equipment
  for line in getStationInformation("channel", network=network, station=station):

    (network,
     station,
     location,
     channel,
     latitude,
     longitude,
     elevation,
     depth,
     azimuth,
     dip,
     description,
     scale,
     frequency,
     units,
     sampleRate,
     starttime,
     endttime) = line.split("|") 

    identifier = "%s.%s.%s.%s" % (network, station, location, channel)
    eposIdentifier = "%s/%s" % (prefix, identifier)

    equipment = Equipment(eposIdentifier, {
      "dct:identifier": eposIdentifier,
      "dct:type": "https://orfeus-eu.org/ns/channel",
      "dct:description": "Specific channel recording ground motion",
      "epos:orientation": azimuth + "/" + dip,
      "dct:title": "Seismic Instrument for %s" % identifier,
      "dcat:contactPoint": ContactPoint("/EPOS/ORFEUS/EIDA/ODC/MRKOYMANS"),
      "schema:manufacturer": Organization("/EPOS/ORGANIZATION/KNMI"),
      "schema:serialNumber": identifier,
      "dct:spatial": Location({
        "locn:geometry": "POINT(%s %s %s)" % (latitude, longitude, elevation)
      }),
      "epos:samplePeriod": getSampleRate(sampleRate), 
      "dct:isPartOf": Equipment("%s/%s.%s" % (prefix, network, station))
    })

    R.register(equipment)

if __name__ == "__main__":

  R = EPOSRDF()

  # Contact point
  CP = ContactPoint("/EPOS/ORFEUS/EIDA/ODC/MRKOYMANS", {
    "schema:contactType": "scientificContact",
    "schema:name": "Mathijs Koymans",
    "schema:email": "koymans@knmi.nl",
    "schema:availableLanguage": "NL, EN",
    "schema:telephone": "030-2206911"
  })

  R.register(CP)

  CON = Concept("SeismicNetwork", {
    "dct:description": "Collection of seismic stations in a seismic network",
    "skos:inScheme": ConceptScheme("Seismology"),
    "skos:prefLabel": "Seismic Network"
  })

  R.register(CON)

  CONS = ConceptScheme("Seismology", {
    "dct:title": "Seismology",
    "dct:description": "It contains the concepts of the Seismology domain"
  })

  R.register(CONS)

  # Register all networks
  networks = registerNetworks("BE")
  networks = list()

  ORG = Organization("/EPOS/ORGANIZATION/KNMI", {
    "schema:identifier": PropertyValue({
      "schema:propertyID": "PIC",
      "schema:value": "999518944"
    }),
    "schema:legalName": "KNMI Dutch Royal Metereological Institute",
    "schema:leiCode": "Whatever",
    "schema:address": PostalAddress({
      "schema:streetAddress": "Utrechtseweg, 297",
      "schema:addressLocality": "De Bilt",
      "schema:postalCode": "3731GA",
      "schema:addressCountry": "The Netherlands"
    }),
    "schema:logo": "http://cdn.knmi.nl/assets/logo_large-1f49334b8856e16f352187f1b52d0edf258976c6329407b0b75f5f109ea012fb.png",
    "schema:url": "http://www.knmi.nl",
    "schema:owns": [Facility("%s/%s" % (prefix, n)) for n in networks]
  })

  R.register(ORG)

  print R.serialize()
