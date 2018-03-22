# EPOS-TURTLE
🐢

Usage:

    from classes.EPOS import EPOSRDF
    from classes import *

    R = EPOSRDF()

    Org = Organization("PIC:997012076", {
      "epos:legalContact": Person("http://orcid.org/0000-0001-7750-7254")
    });

    R.register(Org)
