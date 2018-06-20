import datetime
import requests
import os
import json

from classes.EPOS import EPOSRDF
from classes import *

url = "https://www.orfeus-eu.org/fdsnws/event/1/query?minmagnitude=4&starttime=2018-01-01&format=text"

r = requests.get(url)

R = EPOSRDF()

for line in r.content.split("\n")[-2:-1]:

  (eventId, time, latitude, longitude,
   depth, author, catalog, contributor,
   contributorId, magType, magnitude,
   magAuthor, eventLocationName) = line.split("|")

  shakeMapObject = Dataset("SHAKEMAP:" + eventId, {
    "dct:identifier": "something",
    "dct:title": "EPOS Shakemap",
    "dct:description": "ShakeMap URL for " + eventId,
    "dcat:distribution": Distribution("DISTRIBUTION:" + eventId)
  })

  # Add more metadata
  shakeMapDistribution = Distribution("DISTRIBUTION:" + eventId, {
    "dct:identifier": "something",
    "dcat:accessURL": HydraOperation({
      "hydra:method": "GET"
    })
  })

  R.register(shakeMapObject)
  R.register(shakeMapDistribution)

print R.serialize()
