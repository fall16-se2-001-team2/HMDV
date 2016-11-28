#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------------------------------------
#
# Name                     :Jacob Gantt
# Department Name : Computer and Information Sciences
# File Name                :test_driver.py
# Purpose                  :Handles county objects so that they are each singletons
#
# Author			        : Team Pandas, github.com/fall16-se2-001-team2/HMDV
#                                   Product Owner: Isaac Styles (styles@etsu.edu
# Create Date	            : Nov 14, 2016
#
#-----------------------------------------------------------------------------------------------------------
#
# Modified Date	: Nov 28, 2016
# Modified By		: Jacob Gantt
#
#-------------------------------------------------------------------------------------------------------------


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
            with open("data/Counties_TN_single_lines.json") as f:
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

