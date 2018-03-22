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

  Org = Organization("PIC:997012076", {
    "epos:legalContact": Person("http://orcid.org/0000-0001-7750-7254"),
    "schema:address": PostalAddress({
      "schema:streetAddress": "Utrechtseweg 279"
    })
  })

  R.register(Org)
  
  print R
