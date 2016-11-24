# -*- coding: utf-8 -*-
"""
@author: Matthew Humphrey
"""
import requests
import re
import json
import codecs
from bs4 import BeautifulSoup

def getTopLevelNames ():
    d = codecs.open('servicetree.json', 'r', 'utf-8')
    serviceList = json.load(d)
    d.close()

    names = {}
    topLevels = []

    for l in serviceList:
        if not topLevels.__contains__(l["topLevelName"]):
            topLevels.append(l["topLevelName"])

    topLevels.append("Target Demographics")

    #k = codecs.open('../data/topLevelServices.json','w','utf-8')
    #k.write("[")
    #for t in topLevels:
    #    names["name"] = t
    #    json.dump(names,k)
    #    k.write(",\n")
    #k.write("]")

    return topLevels
