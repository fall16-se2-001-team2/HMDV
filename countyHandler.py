import sys
from county import county

class countyHandler:
    @staticmethod
    def initialize():
        try:
            if countyHandler.countiesList == None:
                print("this should be unreachable code... weird that")
        except AttributeError:
            countyHandler.countiesList = []
            for countyStr in counties:
                countyHandler.countiesList.append( county(countyStr) )

    @staticmethod
    def get_county(name):
        countyHandler.initialize()
        for countyObj in countyHandler.countiesList:
            if( countyObj.name == name ):
                return countyObj
        return none

counties = ["anderson", "bedford", "benton", "bledsoe", "blount", "bradley", "campbell",
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
    "unicoi", "union", "van", "buren", "warren", "washington", "wayne", "weakley",
    "white", "williamson", "wilson"]

"""
import sys
from county import county

class countyHandler:
    @staticmethod
    def Instance():
        try:
            return countyHandler._instance
        except AttributeError:
            countyHandler._instance = singleton()
            return countyHandler._instance

class singleton:
    def __init__(self):
        self.countiesList = []
        for countyStr in counties:
            self.countiesList.append( county(countyStr) )

    def get_county(self, name):
        for countyObj in self.countiesList:
            if( countyObj.name == name ):
                return countyObj
        return none

counties = ["anderson", "bedford", "benton", "bledsoe", "blount", "bradley", "campbell",
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
    "unicoi", "union", "van", "buren", "warren", "washington", "wayne", "weakley",
    "white", "williamson", "wilson"]
"""
