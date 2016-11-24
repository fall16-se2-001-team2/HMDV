import sys
from county import county
import json

class countyHandler:
    @staticmethod
    def initialize():										#singleton design pattern
        try:
            if countyHandler.countiesList == None:
                raise ValueError('Unreachable')
        except AttributeError:
            countyHandler.countiesList = []
            with open("data/Counties_TN.json") as f:
                for line in f:
                    data = json.loads(line)
                    countyHandler.countiesList.append( county(data) )

    @staticmethod
    def get_county(name):
        countyHandler.initialize()
        for countyObj in countyHandler.countiesList:
            if( countyObj.name == name ):
                return countyObj
        return None

"""counties = ["anderson", "bedford", "benton", "bledsoe", "blount", "bradley", "campbell",
    "cannon", "carroll", "carter", "cheatham", "chester", "claiborne", "clay",
    "cocke", "coffee", "crockett", "cumberland", "davidson", "decatur", "deKalb",
    "dickson", "dyer", "fayette", "fentress", "franklin", "gibson", "giles",
    "grainger", "greene", "grundy", "hamblen", "hamilton", "hancock", "hardeman",
    "hardin", "hawkins", "haywood", "henderson", "henry", "hickman", "houston",
    "humphreys", "jackson", "jefferson", "johnson", "knox", "lakev", "lauderdale",
    "lawrence", "lewis", "lincoln", "loudon", "macon", "madison", "marion",
    "marshall", "maury", "mcminn", "mcnairy", "meigs", "monroe", "montgomery",
    "moore", "morgan", "obion", "overton", "perry", "pickett", "polk", "putnam",
    "rhea", "roane", "robertson", "rutherford", "scott", "sequatchie", "sevier",
    "shelby", "smith", "stewart", "sullivan", "sumner", "tipton", "trousdale",
    "unicoi", "union", "van buren", "warren", "washington", "wayne", "weakley",
    "white", "williamson", "wilson"]"""

